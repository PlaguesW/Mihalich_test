import os
import pika

RABBIT_HOST = os.environ.get("RABBITMQ_HOST", "localhost")
EXCHANGE_NAME = "scan_exchange"

def get_connection():# Setup connection to Rabbit
    return pika.BlockingConnection(pika.ConnectionParameters(host=RABBIT_HOST))

def rabbit_init(): # Initialize exchange an queue when app is start 
    connection = get_connection()
    channel = connection.channel()
    # Declare exchange in 'fanout' or 'topic' mode, depending on what we need
    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='fanout', durable=True)
    connection.close()

def publish_message(message: str): # Post a message to an exchange (pub/sub style).
    connection = get_connection()
    channel = connection.channel()
    # Make sure the exchange exists
    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='fanout', durable=True)
    # Publish
    channel.basic_publish(
        exchange=EXCHANGE_NAME,
        routing_key='',
        body=message.encode("utf-8")
    )
    connection.close()
 # An example of a simple consumer that subscribes to all messages from an exchange. We would typically run it in a separate process/thread.
def start_consumer(): 
    connection = get_connection()
    channel = connection.channel()
    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='fanout', durable=True)

    # Create a temporary queue (or named one), bind to exchange
    queue_result = channel.queue_declare(queue='', exclusive=True)
    queue_name = queue_result.method.queue
    channel.queue_bind(exchange=EXCHANGE_NAME, queue=queue_name)

    def callback(ch, method, properties, body):
        print("[Consumer] Received:", body.decode("utf-8"))
        # Here we can process the message: parse JSON, write to the DB, etc.

    channel.basic_consume(
        queue=queue_name,
        on_message_callback=callback,
        auto_ack=True
    )
    print("[Consumer] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()
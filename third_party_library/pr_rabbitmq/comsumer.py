import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='steverocket')


def callback(ch, method, properties, body):
    print(f'[x] Received {body}')


channel.basic_consume(queue='steverocket', on_message_callback=callback, auto_ack=True)
print('[*] Waiting for messages. To exit press CTRL + C')
channel.start_consuming()

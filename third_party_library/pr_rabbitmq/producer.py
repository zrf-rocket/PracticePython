import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='steverocket')

channel.basic_publish(exchange='', routing_key='steverocket', body='my name is steverocket')
print('[x] Sent "hello!"')
connection.close()

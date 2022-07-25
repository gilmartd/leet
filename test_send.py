import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
queue = "hello"
channel.queue_declare(queue=queue)
routing_key = 'hello'
body = "ghijk1234c"
channel.basic_publish(exchange='', routing_key=routing_key, body=body)
print(" [x] Sent " + body)
connection.close()

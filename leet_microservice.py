import os
import pika
import sys

def send(leet):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    queue = "leet"
    channel.queue_declare(queue=queue)
    routing_key = 'leet'
    channel.basic_publish(exchange='', routing_key=routing_key, body=leet)
    print(" [x] Sent " + leet)
    connection.close()

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    table = {

        # Uppercase Alphabets
        'A': '4', 'B': '8', 'E': '3', 'H': '#',
        'I': '1', 'O': '0', 'S': '5', 'T': '7', 'Z': '2',

        # Lowercase Alphabets
        'a': '@', 'b': '6', 'c': '(', 'g': '9', 'i': '!', 'z': '%',

        # Numbers
        '1': 'l', '2': 'Z', '3': 'E', '4': 'A',
        '5': 'S', '6': 'b', '8': 'B',
        '9': 'q', '0': '2',
    }

    def callback(ch, method, properties, body):
        print(" [x] Received %r " % body)
        password = str(body)
        leet = ""
        for char in range(2, len(password)):
            if password[char] in table.keys():
                leet += table[password[char]]
            else:
                leet += password[char]
        send(leet)
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)


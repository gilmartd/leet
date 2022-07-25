A. How to request data from the "leetspeak" converter:
The converter when started locally listens on RabbitMQ default connection channel using
 
queue: "hello"

routing_key: "hello"

The microservice accepts strings of any length and will convert them to "leetspeak" for more secure passwords. 
An example request would be to send "ABCDefgI" in the body of the .basic_publish like:

channel.basic_publish(exchange='', routing_key="hello", body="ABCDefgI")

B. The microservice will send back the converted password using RabbitMQ default connection channel with 

queue = "leet"

routing_key = "leet"

the converter will send back a string with the same length as the original string, but it might have numbers or symbols in place of other characters. The send line of code is:
    queue = "leet"
    channel.queue_declare(queue=queue)
    routing_key = 'leet'
    channel.basic_publish(exchange='', routing_key=routing_key, body=leet)
    
C.

![image](https://user-images.githubusercontent.com/91555362/180724944-3444fb69-6eea-472d-858b-1dfa49c162c9.png)

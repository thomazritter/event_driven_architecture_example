import pika
import time

# Estabelece conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declara a mesma fila para garantir que ela exista
channel.queue_declare(queue='hello')

print(' [*] Aguardando mensagens.')

# Define a função de callback para processar mensagens recebidas
def callback(ch, method, properties, body):
    print(f" [x] Recebido {body.decode()}")

# Configura o consumidor para usar a função de callback
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

# Inicia o consumo de mensagens
channel.start_consuming()
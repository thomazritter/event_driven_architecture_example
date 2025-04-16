import pika

# Estabelece conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declara uma fila chamada 'hello'
channel.queue_declare(queue='hello')

print("Digite mensagens para enviar à fila. Digite 'exit' para sair.")

while True:
    message = input("Mensagem: ")
    if message.lower() == 'exit':
        break
    channel.basic_publish(exchange='', routing_key='hello', body=message.encode())
    print(f" [x] Enviado '{message}'")

# Fecha a conexão
connection.close()
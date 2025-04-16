# event_driven_architecture_example

This project was made with the goal of testing out the EDA through RabbitMQ

# How to test this out
1.  Clone repository
2.  Download `pika` library (RabbitMQ)
3.  Download Docker
4.  Execute
`docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4-management`
5. Cd to your cloned repository and execute
- `py consumer.py`
- `py producer.py`
6. Feel free to go to `http://localhost:15672` to observe everything working. Use guest as both user and password
7. Write everything you want to push to the queue in the producer terminal

Enjoy!

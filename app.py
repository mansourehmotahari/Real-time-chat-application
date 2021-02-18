from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, emit
from kafka import KafkaProducer, KafkaConsumer, TopicPartition
import uuid

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

BOOTSTRAP_SERVERS = '127.0.0.1:9092'
#TOPIC_NAME = 'stackbox'


@app.route('/')
@cross_origin()
def home():
    return 'Flask is running!'

""" Kafka endpoints """


@socketio.on('connect', namespace='/kafka')
def test_connect():
    emit('logs', {'data': 'Connection established'})


@socketio.on('kafkaconsumer1', namespace="/kafka")
def kafkaconsumer1(message,TOPIC_NAME):
    consumer = KafkaConsumer(bootstrap_servers=BOOTSTRAP_SERVERS,group_id='consumer-1',
                         auto_offset_reset='latest',
                         enable_auto_commit=True)

    tp = TopicPartition(TOPIC_NAME, 0)
    # register to the topic
    consumer.assign([tp])

    # obtain the last offset value
    consumer.seek_to_end(tp)
    lastOffset = consumer.position(tp)
    print(lastOffset)

    consumer.seek_to_beginning(tp)
    message=''
    for message in consumer:
        if message.offset == lastOffset - 1:
            emit('kafkaconsumer1', {'data': message.value.decode('utf-8')}, broadcast=True)
            break
    consumer.close()

    
    
@socketio.on('kafkaconsumer2', namespace="/kafka")
def kafkaconsumer2(message,TOPIC_NAME):
    print("are")
    consumer = KafkaConsumer(bootstrap_servers=BOOTSTRAP_SERVERS,group_id='consumer-2',
                         auto_offset_reset='latest',
                         enable_auto_commit=True)
    
    tp = TopicPartition(TOPIC_NAME, 0)
    # register to the topic
    consumer.assign([tp])
    consumer.seek_to_end(tp)
    lastOffset = consumer.position(tp)
    consumer.seek_to_beginning(tp)
    #emit("kafkaconsumer2",{'data':message},broadcast=True)
    for message in consumer:

        if message.offset == lastOffset - 1:
            emit('kafkaconsumer2', {'data': message.value.decode('utf-8')}, broadcast=True)
            break
    consumer.close()


@socketio.on('kafkaproducer1', namespace="/kafka")
def kafkaproducer1(message,TOPIC_NAME):
    print("mansoureh")
    producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS)
    producer.send(TOPIC_NAME, value=bytes(str(message), encoding='utf-8'), key=bytes(str(uuid.uuid4()), encoding='utf-8'))
    emit('logs1', {'data': 'Added ' + message + ' to topic'+TOPIC_NAME})
    emit('kafkaproducer1', {'data': message})
    producer.close()
    
    kafkaconsumer2(message,TOPIC_NAME)
    
        
        
@socketio.on('kafkaproducer2', namespace="/kafka")
def kafkaproducer2(message,TOPIC_NAME):
          
    producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS)
    producer.send(TOPIC_NAME, value=bytes(str(message), encoding='utf-8'), key=bytes(str(uuid.uuid4()), encoding='utf-8'))
    emit('logs2', {'data': 'Added ' + message + ' to topic'+TOPIC_NAME})
    emit('kafkaproducer2', {'data': message})
    producer.close()
    
    kafkaconsumer1(message,TOPIC_NAME)
    


if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=80)

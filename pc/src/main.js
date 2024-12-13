import mqtt from 'mqtt'

const client = mqtt.connect('ws://localhost:9001');
client.options.username = 'picoW';
client.options.password = 'picoW';

// mosquitto version 1.6.9 works with websockets, newest does not. Best to use this one if you want to test it.
// mosquitto config file probably needs to be changed to allow websockets

client.on('connect', () => {
    console.log('Connected to MQTT broker')
    client.subscribe('temperature');
    client.subscribe('pressure');
    client.subscribe('humidity');
});

client.on('message', (topic, message) => {
    const messageString = message.toString();
    if (topic === 'temperature') {

        document.getElementById('temperature').textContent = messageString;

    } else if (topic === 'pressure') {

        document.getElementById('pressure').textContent = messageString;

    } else if (topic === 'humidity') {

        document.getElementById('humidity').textContent = messageString;
    }
});

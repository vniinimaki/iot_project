import mqtt from 'mqtt'

const client = mqtt.connect('ws://localhost:9001');
client.options.username = 'picoW';
client.options.password = 'picoW';

// mosquitto version 1.6.9 works with websockets, newest does not.

client.on('connect', () => {
    console.log('Connected to MQTT broker')
    client.subscribe(['temperature', 'pressure', 'altitude']);
});

client.on('message', (topic, message) => {
    let messageFloat = parseFloat(message.toString()).toFixed(1);
    let messageString;

    switch (topic) {
        case 'temperature':
            messageString = messageFloat + '°C';

            if (messageFloat >= 24) {
                document.getElementById(topic).style.color = 'orange';
            } else if (messageFloat < 20) {
                document.getElementById(topic).style.color = 'lightblue';

            } else { document.getElementById(topic).style.color = 'whitesmoke'; }

            break;

        case 'pressure':
            messageString = messageFloat + ' hPa';
            break;

        case 'altitude':
            messageString = messageFloat + ' m';
            break;
    }

    document.getElementById(topic).textContent = messageString;
});

document.getElementById('time').innerText = new Date().toLocaleTimeString();
setInterval(() => {
    document.getElementById('time').innerText = new Date().toLocaleTimeString();
}, 1000);

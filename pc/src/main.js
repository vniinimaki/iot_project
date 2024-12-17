import mqtt from 'mqtt'
import aesjs from 'aes-js'

const client = mqtt.connect('ws://localhost:9001');
client.options.username = 'picoW';
client.options.password = 'picoW';

// mosquitto version 1.6.9 works with websockets, newest does not.

let tempMin, tempMax, pressureMin, pressureMax, altitudeMin, altitudeMax;

let lastMessage = 0;
let previousMessage = 0;
let latencies = [];
const key = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6];
const aesEcb = new aesjs.ModeOfOperation.ecb(key);

const measureLatency = () => {
    previousMessage = lastMessage;
    lastMessage = new Date().getTime();
    latencies.push(lastMessage - previousMessage);
    if (latencies.length > 128) {
        latencies.shift();
    }
}

client.on('connect', () => {
    console.log('Connected to MQTT broker')
    client.subscribe(['temperature', 'pressure', 'altitude']);
});

client.on('message', (topic, message) => {
    let decryptedBytes = aesEcb.decrypt(message);
    let messageCrypt = aesjs.utils.utf8.fromBytes(decryptedBytes);

    // toFixed returns a string, because JavaScript, so we need to parse it to a float again for the comparasions to work
    let messageFloat = parseFloat(parseFloat(messageCrypt.toString()).toFixed(1));

    // For testing with unencrypted messages
    // let messageFloat = parseFloat(parseFloat(message.toString()).toFixed(1));
    let messageString;

    switch (topic) {
        // Set default values for min and max
        case 'temperature':
            // log the time it takes between messages
            measureLatency()

            if (tempMin === undefined) {
                tempMin = tempMax = messageFloat;
            }

            tempMax = messageFloat > tempMax ? messageFloat : tempMax;
            tempMin = messageFloat < tempMin ? messageFloat : tempMin;

            document.getElementById('temperature-min').textContent = tempMin + '°C';
            document.getElementById('temperature-max').textContent = tempMax + '°C';

            messageString = messageFloat + '°C';
            break;

        case 'pressure':
            // log the time it takes between messages
            measureLatency()

            // Set default values for min and max
            if (pressureMin === undefined) {
                pressureMin = pressureMax = messageFloat;
            }

            pressureMax = (messageFloat > pressureMax) ? messageFloat : pressureMax;
            pressureMin = (messageFloat < pressureMin) ? messageFloat : pressureMin;

            document.getElementById('pressure-min').textContent = pressureMin + ' hPa';
            document.getElementById('pressure-max').textContent = pressureMax + ' hPa';

            messageString = messageFloat + ' hPa';
            break;

        case 'altitude':
            // log the time it takes between messages
            measureLatency()

            // Set default values for min and max
            if (altitudeMin === undefined) {
                altitudeMin = altitudeMax = messageFloat;
            }

            altitudeMax = messageFloat > altitudeMax ? messageFloat : altitudeMax;
            altitudeMin = messageFloat < altitudeMin ? messageFloat : altitudeMin;

            document.getElementById('altitude-min').textContent = altitudeMin + ' m';
            document.getElementById('altitude-max').textContent = altitudeMax + ' m';

            messageString = messageFloat + ' m';
            break;
    }

    document.getElementById(topic).textContent = messageString;
});

setInterval(() => {
    document.getElementById("last").textContent = 'Average latency: ' + (latencies.reduce((a, b) => a + b, 0) / latencies.length).toFixed(2) + ' ms'
}, 1000);

import mqtt from 'mqtt'

const client = mqtt.connect('ws://localhost:9001');
client.options.username = 'picoW';
client.options.password = 'picoW';

// mosquitto version 1.6.9 works with websockets, newest does not.

let tempMin, tempMax, pressureMin, pressureMax, altitudeMin, altitudeMax;

client.on('connect', () => {
    console.log('Connected to MQTT broker')
    client.subscribe(['temperature', 'pressure', 'altitude']);
});

client.on('message', (topic, message) => {
    let messageCrypt = message
    let messageFloat = parseFloat(message.toString()).toFixed(1);
    let messageString;

    switch (topic) {
        // Set default values for min and max
        case 'temperature':
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
            // Set default values for min and max
            if (pressureMin === undefined) {
                pressureMin = pressureMax = messageFloat;
            }

            pressureMax = (messageFloat - 1000 > pressureMax - 1000) ? messageFloat : pressureMax;
            pressureMin = (messageFloat - 1000 < pressureMin - 1000) ? messageFloat : pressureMin;

            document.getElementById('pressure-min').textContent = pressureMin + ' hPa';
            document.getElementById('pressure-max').textContent = pressureMax + ' hPa';

            messageString = messageFloat + ' hPa';
            break;

        case 'altitude':
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

document.getElementById('time').textContent = new Date().toLocaleTimeString();
setInterval(() => {
    document.getElementById('time').textContent = new Date().toLocaleTimeString();
}, 1000);

import mqtt from 'mqtt'

const client = mqtt.connect('ws://localhost:9001');
client.options.username = 'picoW';
client.options.password = 'picoW';

const renderImage = () => {
    const binaryData = new Uint8Array(imageChunks.reduce((acc, chunk) => acc.concat(Array.from(chunk)), []));
    // Blob contains extra data at the end, so we need to trim it to the actual image size
    let base64String = '';
    for (let i = 0; i < binaryData.length; i++) {
        base64String += String.fromCharCode(binaryData[i]);
    }

    base64String = btoa(base64String.slice(0, imageSize));

    document.getElementById('image').src = 'data:image/jpeg;base64,' + base64String + `#${new Date().getTime()}`;
}

let numberOfChunks = 0;
let imageChunks = [];
let imageSize = 0;

// mosquitto version 1.6.9 works with websockets, newest does not. Best to use this one if you want to test it.
// mosquitto config file probably needs to be changed to allow websockets

client.on('connect', () => {
    console.log('Connected to MQTT broker')
    client.subscribe('text');
    client.subscribe('images');
    client.subscribe('chunkSize');
    client.subscribe('imageSize');
});

client.on('message', (topic, message) => {
    const messageString = message.toString();
    if (topic === 'text') {
        console.log('Received message:', messageString);
        const list = document.getElementById('messages');
        list.appendChild(document.createElement('p')).textContent = messageString;

    } else if (topic === 'chunkSize') {
        numberOfChunks = parseInt(messageString);

    } else if (topic === 'imageSize') {
        imageSize = parseInt(messageString);

    } else if (topic === 'images') {
        if (imageChunks.length < numberOfChunks) {
            imageChunks.push(message);
        }

        if (imageChunks.length == numberOfChunks) {
            console.log('All chunks received', imageChunks.length);
            renderImage();
        }
    }
});

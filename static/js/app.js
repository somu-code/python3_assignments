const socket = io();
const form = document.getElementById('form');
const input = document.getElementById('input');
const messages = document.getElementById('messages');

form.addEventListener(
    'submit',
    event => {
        event.preventDefault();
        socket.emit('message', input.value);
        input.value = '';
    }
)

socket.on(
    'message',
    message => {
        const li = document.createElement('li');
        li.innerText = message;
        messages.appendChild(li);
    }
);
# SwitchDin_Interview

Requirements:
    rabbitmq with websocket plugin enabled (or change the port in mainScript.js for other broker)
    paho for python
    the rest are contained (jquery, pahojs, velocityjs)

Files:
receiver.py
    a small python script that subscribes to the localhost:1883 rng topic and prints any messaged recieved

emitter.py
    emitts a random number message the rng topic on both ports 1883 (mqtt) and 15675 (mqtt_ws currently broken and commented out)

mainScript.js 
    attempts to connect to localhost:15675 and recieve the rng message then change a small svgs height to that value. Currently this is controlled by the text input at the top since I kept getting a websocket handshape error
    and was unable to resolve it.

SwitchDin.html
    the main display site for the challenge

Instructions
    install and configure Requirements
    run receiver.py
    open SwitchDin.html in browser of your choice
    run emitter.py
    notice the log in receiver (and handshake error if you uncomment the ws part of the file...)
    change the value in the number input for the html and notice the black box animate.
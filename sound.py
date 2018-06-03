import time
import vision
import sound2text
import text
import tone
import socket
import sys
import os
import feedback


text_info = {}
emo_info = ''


def keyword():
    global text_info
    global emo_info
    s_time = time.time()
    transcript = sound2text.sound2text()
    text_info = text.text(transcript)
    emo_info = tone.tones(transcript)
    print("The current text infomation is:" + str(text_info))
    print("The current tone of discussion is:" + emo_info)
    # if (time.time() - s_time > 100):
    # break


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10001)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

print('succeed in connecting to {} port {}'.format(*server_address))
try:
    # Send data
    # message = b'This is the message.  It will be repeated.'
    while True:
        keyword()
    # message = input()
        if (text_info["sentiment"] == "negative"):
            os.system("say we are really sorry about that. please give us some suggestions.")
        if (text_info["sentiment"] == "neutral"):
            os.system("say are you pleased with this experience?")
        else:
            os.system("say we are glad to give you a pleasant experience!")
        feedback.send_request("奥利奥", 16, text_info["sentiment"], text_info["keyword"], emo_info)
        message = str(text_info) + emo_info
        print('sending {!r}'.format(message))
        sock.sendall(message.encode())

    # # Look for the response
    # amount_received = 0
    # amount_expected = len(message)

    # while amount_received < amount_expected:
    #     data = sock.recv(16)
    #     amount_received += len(data)
    #     print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()

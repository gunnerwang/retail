import cv2
import datetime
import os
from face import *
import threading
import time
import vision
import sound2text
import text
import tone
import socket
import sys
from vision import image

text_info = dict({})
emo_info = ""

def receive_msg(connection, client_address):
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            if data:
                print('received {!r}'.format(data.decode()))
                # if data:
                #     print('sending data back to the client')
                #     connection.sendall(data)
                # else:
                #     print('no data from', client_address)
                #     break

    finally:
        # Clean up the connection
        print("close")
        connection.close()

def server():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('localhost', 10001)
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        threading.Thread(target=receive_msg, args=(connection, client_address)).start()

def main():
    timeF = 10
    OUTPUT_DIR = "image"
    c = 1
    cap = cv2.VideoCapture(0)
    if not os.path.isdir(OUTPUT_DIR):
        os.system("mkdir {dir}".format(dir=OUTPUT_DIR))

    thread2 = threading.Thread(target=server)
    thread2.start()

    while True:
        ret, img = cap.read()
        output_dir = os.path.join(
            OUTPUT_DIR, datetime.datetime.now().strftime('%H_%M_%S'))
        cv2.imshow('img', vision.deal_img(img))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    #os.system("rm -r image")
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
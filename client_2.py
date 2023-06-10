import sys
import socket
import logging
import time

# set basic logging
logging.basicConfig(level=logging.INFO)

try:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('172.18.0.5', 32444)
    logging.info(f"connecting to {server_address}")
    sock.connect(server_address)

    # Send file content
    with open('testfile.txt', 'r') as f:
        message = f.read()
    logging.info(f"sending file content")
    sock.sendall(message.encode())

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(1024)
        amount_received += len(data)
        logging.info(f"{data}")

    times = 0
    while (times < 10):
        times += 1
        logging.info('...')
        time.sleep(2)
        
except Exception as ee:
    logging.info(f"ERROR: {str(ee)}")
    exit(0)
finally:
    logging.info("closing")
    sock.close()
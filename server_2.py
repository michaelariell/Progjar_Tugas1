import sys
import socket
import logging
import time

logging.basicConfig(level=logging.INFO)

try:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)

    # Bind the socket to the port
    server_address = ('0.0.0.0', 32444) #--> gunakan 0.0.0.0 agar binding ke seluruh ip yang tersedia

    logging.info(f"starting up on {server_address}")
    sock.bind(server_address)
    # Listen for incoming connections
    sock.listen(1)
    #1 = backlog, merupakan jumlah dari koneksi yang belum teraccept/dilayani yang bisa ditampung, diluar jumlah
    #             tsb, koneks akan direfuse
    while True:
        # Wait for a connection
        logging.info("waiting for a connection")
        connection, client_address = sock.accept()
        logging.info(f"connection from {client_address}")
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            # 1024 -> merupakan buffersize, jumlah maksimum data yang bisa diterima sekaligus
            # buffersize lebih baik diset dalam power of 2 contoh: 1024, 32, 4096
            logging.info(f"received {data}")
            if data:
                logging.info("sending back data")
                connection.sendall(data)
            else:
                # print(f"no more data from {client_address}")
                break
        # Clean up the connection
        # times = 0
        # while (times < 10):
        #     times += 1
        #     logging.info('...')
        #     time.sleep(2)
            
        connection.close()
except Exception as ee:
    logging.log(logging.INFO, f"ERROR: {str(ee)}")
finally:
    logging.log(logging.INFO, 'closing')
    sock.close()
# Provides access to the BSD socket API (interface). It includes function calls that can be used in an application.
import socket 

# Create the actual socket object using socket.socket(), and the type is specified as socket.SOCK_STREAM which results in TCP as the default protocol. 
# Saved as a variable for referencing later.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# I will define the host as the loopback address and Port as 9999.
HOST = '127.0.0.1'
PORT = 9999

# Tell the socket which address and port to listen on.
# At this point I realised, I could have used s.bind(('127.0.0.1',9999))
s.bind((HOST, PORT))

# Accept upto 5 connections
s.listen(5)

while True:
    conn, addr = s.accept()

    # The interesting part is that for every new connection accepted, a new socket opens.
    # The original socket in socket.socket() is not used by the kernel to actually exchange data.
    # .bind() and .listen() flip that socket into a LISTEN state.
    # The kernel also attaches two internal queues to it: 1) The SYN queue and; 2) The Accept queue.
    # .accept() is actually what takes one completed connection from the accept queue and allocates it a brand new socket.
    # That brand new socket will have its own, independent Transmission Control Block (TCB)
    # i.e. TCB is a data structuring tracking connections. 

    data = conn.recv(1024)
    conn.send(data)

    # After receiving data (setting a buffer of 1kb) and echoing it back to the client, we need to close the connection.
    # The socket I will close is conn, instead of s so that it can continue listening for other connections.

    conn.close()




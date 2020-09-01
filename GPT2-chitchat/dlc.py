from socketserver import BaseRequestHandler, TCPServer

# import the socketserver module of Python

import socketserver


# Create a Request Handler

# In this TCP server case - the request handler is derived from StreamRequestHandler

class EchoHandler(socketserver.StreamRequestHandler):

    # handle() method will be called once per connection

    def handle(self):
        # Receive and print the data received from client

        print("Recieved one request from {}".format(self.client_address[0]))

        msg = self.rfile.readline().strip()

        print("Data Recieved from client is:".format(msg))

        print(msg)

        # Send some data to client

        self.wfile.write("Hello Client....Got your message".encode())


# Create a TCP Server instance

aServer = socketserver.TCPServer(("127.0.0.1", 9090), EchoHandler)

# Listen for ever

aServer.serve_forever()


if __name__ == '__main__':
    serv = TCPServer(('', 30000), EchoHandler)
    print("server started at 30000")
    serv.serve_forever()
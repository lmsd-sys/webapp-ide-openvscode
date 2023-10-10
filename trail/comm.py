import socket

# # Create a socket and bind it to the desired port
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(('localhost', 8090))

# # Start listening for incoming connections
# server_socket.listen(1)

# print("listening on localhost:8090")

# while True:
#     # Accept incoming connections
#     client_socket, client_address = server_socket.accept()

#     # Receive the message from the client
#     message = client_socket.recv(1024).decode()

#     # Log the message to 'log.txt'
#     with open('log.txt', 'a') as log_file:
#         log_file.write(message + '\n')

#     # Send the same message back to the client
#     client_socket.sendall(message.encode())

#     # Close the connection
#     client_socket.close()



# def init_socket(server_socket: socket.socket):
#     server_socket.bind(("localhost", 8090))
#     server_socket.listen(1)
# def get_message_from_native_app(server_socket: socket.socket) -> tuple[str, socket.socket]:
#     client_socket, _ = server_socket.accept()
#     data = client_socket.recv(4096).decode()
#     return data, client_socket
# def start():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
#         init_socket(server_socket)

#         message_count = 0
#         while True:
#             msg, client_socket = get_message_from_native_app(server_socket)
#             print(f"got message: {msg}")
#             client_socket.sendall(msg.encode())
#             client_socket.close()
# start()


import socket

def init_socket(server_socket: socket.socket):
    server_socket.bind(("localhost", 8090))
    server_socket.listen()

def get_message_from_native_app(client_socket: socket.socket) -> str:
    data = client_socket.recv(4096).decode()
    return data

def start():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        init_socket(server_socket)

        while True:
            client_socket, _ = server_socket.accept()
            print("Accepted a connection.")

            while True:
                msg = get_message_from_native_app(client_socket)
                print(f"got message: {msg}")

                client_socket.sendall(msg.encode())
                print("finished cycle")

            client_socket.close()

if __name__ == "__main__":
    start()

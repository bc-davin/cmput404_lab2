import socket

#target and host
host="www.google.com"
port=80

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect((host,port))

#send an HTTP GET request
request="GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(host)
client_socket.send(request.encode())

# Receive and print the response
response = b""
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    response += data

print(response.decode())

# Close the socket
client_socket.close()
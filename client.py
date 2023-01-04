import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

server_address = ("localhost", 1234)

client.connect(server_address)

data = input()
data_bytes = data.encode("utf-8")
client.send(data_bytes)


data_bytes = client.recv(4096)
data = data_bytes.decode("utf-8")
print(data)
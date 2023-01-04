import select
import socket


read = []
write = []
errors = []

server_address = ("", 1234)


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP) as server:

        server.bind(server_address)
        server.listen(1)

        read.append(server)

        while(True):
            readable, writeable, exceptional = select.select(read, write, errors)

            for sock in readable:
                if sock == server:
                    connection, client_address = server.accept()
                    print("Connected by", client_address)
                    read.append(connection)
                else:
                    data_bytes = sock.recv(4096)
                    data = data_bytes.decode("utf-8")

                    data = data.upper()

                    data_bytes = data.encode("utf-8")
                    sock.send(data_bytes)


if __name__ == "__main__":
    main()
    
import asyncio

import settings


async def main(host, port):
    server = await asyncio.start_server(handle_connection, host, port)
    async with server:
        await server.serve_forever()


async def handle_connection(reader, writer):
    writers.add(writer)
    
    while True:
        try:
            bytes = await reader.read(1024)
        except ConnectionError:
            break

        if not bytes:
            break
        
        await broadcast(bytes, writer)

    writers.remove(writer)

    writer.close()


async def broadcast(bytes, sender):
    for writer in writers:
                if writer != sender:
                    writer.write(bytes)
                    await writer.drain()


HOST, PORT = settings.HOST, settings.PORT

writers = set()

if __name__ == "__main__":
    asyncio.run(main(HOST, PORT))

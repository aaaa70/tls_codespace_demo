import asyncio, ssl

HOST = "localhost"
PORT = 8888
CAFILE = "cert.pem"

async def tcp_client():
    ssl_ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=CAFILE)
    ssl_ctx.check_hostname = False
    reader, writer = await asyncio.open_connection(HOST, PORT, ssl=ssl_ctx)
    print("Connected to server (TLS)")
    try:
        for msg in ["hello server", "secure message", "bye"]:
            line = msg + "\n"
            writer.write(line.encode())
            await writer.drain()
            data = await reader.readline()
            print("Server replied:", data.decode().rstrip())
    finally:
        writer.close()
        await writer.wait_closed()
        print("Connection closed")

if __name__ == "__main__":
    asyncio.run(tcp_client())

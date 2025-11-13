import asyncio, ssl

HOST = "0.0.0.0"
PORT = 8888
CERTFILE = "cert.pem"
KEYFILE = "key.pem"

async def handle(reader, writer):
    addr = writer.get_extra_info("peername")
    print(f"Connected: {addr}")
    try:
        while True:
            data = await reader.readline()
            if not data:
                break
            text = data.decode().rstrip()
            print(f"Received from {addr}: {text}")
            resp = f"Echo: {text}\n"
            writer.write(resp.encode())
            await writer.drain()
    except Exception as e:
        print("Connection error:", e)
    finally:
        writer.close()
        await writer.wait_closed()
        print(f"Disconnected: {addr}")

async def main():
    ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_ctx.load_cert_chain(certfile=CERTFILE, keyfile=KEYFILE)
    server = await asyncio.start_server(handle, HOST, PORT, ssl=ssl_ctx)
    addrs = ", ".join(str(sock.getsockname()) for sock in server.sockets)
    print(f"Server running on {addrs} (TLS)")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())

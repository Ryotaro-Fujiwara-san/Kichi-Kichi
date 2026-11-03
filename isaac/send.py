import socket
import sys

path = sys.argv[1]
with open(path, encoding="utf-8") as f:
    source = f.read()

with socket.create_connection(("127.0.0.1", 8226), timeout=10) as s:
    s.sendall(source.encode("utf-8"))
    s.shutdown(socket.SHUT_WR)
    s.settimeout(60)
    chunks = []
    while True:
        data = s.recv(4096)
        if not data:
            break
        chunks.append(data)
print(b"".join(chunks).decode("utf-8", "replace"))

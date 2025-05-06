from pythonosc import dispatcher, osc_server

def print_handler(address, *args):
    print(f"Received on {address}: {args}")

dispatcher = dispatcher.Dispatcher()
dispatcher.map("/test", print_handler)

ip = "127.0.0.1"  # localhost
port = 11235      # must match what Bonsai is sending to

server = osc_server.ThreadingOSCUDPServer((ip, port), dispatcher)
print(f"Listening on {ip}:{port}")
server.serve_forever()
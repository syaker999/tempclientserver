import socket

def fahrenheit_to_celsius(temp_f):
    temp_c = (temp_f - 32) * 5 / 9
    return temp_c

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 8888))
    s.listen()
    print("Server started at 192.168.85.132:8888")

    while True:
        c, address = s.accept()
        print(f"Connection from {address} has been established.")
        temp_f = c.recv(1024)
        temp_f = float(temp_f.decode())
        temp_c = fahrenheit_to_celsius(temp_f)
        c.send(str(temp_c).encode())
        c.close()

main()

import socket

def main():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(("192.168.85.132", 8888))
    temp_f = float(input("Enter temperature in Fahrenheit: "))
    c.send(str(temp_f).encode())
    temp_c = c.recv(1024)
    temp_c = float(temp_c.decode())
    print(f"Temperature in Celsius: {temp_c}")
    c.close()

main()

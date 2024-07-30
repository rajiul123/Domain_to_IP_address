import socket

domain_name = input("Enter your targeted domain name: ")

ip = socket.gethostbyname(domain_name)

print("IP for {} : {}".format(domain_name, ip))

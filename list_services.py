'''
Shin Tran
Python 230
Assignment 2

Write a python function that lists the services provided by a given range of ports.
- accept the lower and upper bounds as arguments
- provide sensible defaults
- Ensure that it only accepts valid port numbers (0-65535)
'''

import socket

def print_services(low_num, high_num):
    for port_num in range(low_num, high_num + 1):
        try:
            service = socket.getservbyport(port_num)
            print("{} - {}".format(port_num, service))
        except:
            continue


if __name__ == '__main__':
    low_num = int(input("Enter a number between 0 and 65535: "))
    high_num = int(input("Enter another number between 0 and 65535: "))
    if (0 <= low_num <= high_num <= 65535):
        print_services(low_num, high_num)
    else:
        print("Port numbers invalid.")

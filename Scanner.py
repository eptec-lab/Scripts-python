# AUTHOR: CLAUDE NGASSA
# **************************SIMPLE PORT SCANNER USING ARGPARSE(OPTPARSE DEPRECATED) AND THREADS*************************#

import socket  # Socket module
from threading import Thread  # Thread class
import argparse  # Parser
from colorama import Fore  # Color


class Thread_action(Thread):  # Class inherited from threading class
    def __init__(self, target, args) -> None:
        # Defining the constructor with his arguments and inherited function from threading
        Thread.__init__(self, target=target, args=args)

        def run(self):  # Start a new instance of a thread
            print("Thread started")


def portScan(ip, port):
    # We'll create a new socket per threads
    try:
        listener = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)  # Defining a socket
        listener.settimeout(2)  # Time out of 2 seconds between each connection
        listener.connect((socket.gethostbyname(ip), port))
        print(Fore.GREEN+f"{port}", Fore.GREEN+"\topen",
              Fore.GREEN+f"\t{socket.getservbyport(port)}")  # Port identification
        listener.close()  # Close the socket on this thread
    except socket.error as e:
        pass  # esacpe the function


if __name__ == "__main__":  # The main function like in C or Java programming

    parser = argparse.ArgumentParser(
        description="Simple and sophisticated portscanner with ArgParse and threading",  # Description
        epilog="See more informations on argpase on https://docs.python.org/3/library/argparse.html")  # Docs for argparse
    parser.add_argument(
        "-H", "--host", help="specify hostname to run on")  # Host definition
    parser.add_argument(
        "-p", "--port", help="port number to run on", default=1000)  # Host definition
    args = parser.parse_args()
    if args.host == None and args.port == None:  # We need to check the amount of arguments
        raise Exception("".join(parser.format_help()))
    elif args.host == None:
        raise Exception("The host might be defined")  # Host not defined
    # elif args.port == None:
    #     raise Exception("The port might be defined")  # port not defined
    # We save both the port and the host in variables
    hostname = args.host
    portnum = args.port  # it will scan the first 1000 ports if the port is not defined
    print(f"\nScanning opened ports for address {hostname}\n")
    print("Port", "\tState", "\tService")  # Interface
    if portnum == 1000:
        for i in range(1, portnum):  # the first thousand
            proc1 = Thread_action(portScan, args=(hostname, i))
            proc1.start()
    if str(portnum).find("-"):  # large number of ports
        res = [int(i) for i in str(portnum).split("-")]
        for i in range(int(res[0]), int(res[-1])+1):
            proc1 = Thread_action(portScan, args=(hostname, i))
            proc1.start()
            proc1.join()
    else:  # Just for one specific port
        proc1 = Thread_action(portScan, args=(hostname, portnum))
        proc1.start()

Server - Client
This is a Python program for creating a simple server-client communication. The program allows users to choose whether they want to run it as a server or client. It supports the following features:

IP address and port number can be defined by the user.
The user can set the interval for sending data and the size of the data to be sent.
The program can calculate the throughput, jitter, and OWD (one-way delay) metrics.

Libraries
socket
time
argparse

Functions
input_argument(): This function is used to get the input arguments from the user. The arguments include the IP address, port number, reference interval, server/client choice, data size, and time duration.
throughput_Start(thr): This function starts the timer for measuring throughput. The thr parameter is used to indicate whether the user wants to measure throughput.
throughput_End(thr): This function ends the timer for measuring throughput and calculates the throughput based on the amount of data sent and the time it took to send it. The thr parameter is used to indicate whether the user wants to measure throughput.
jitter_Start(jit): This function starts the timer for measuring jitter. The jit parameter is used to indicate whether the user wants to measure jitter.
jitter_End(jit): This function ends the timer for measuring jitter and calculates the mean time of jitter. The jit parameter is used to indicate whether the user wants to measure jitter.
OWD_Start(OWD): This function starts the timer for measuring one-way delay (OWD). The OWD parameter is used to indicate whether the user wants to measure OWD.
OWD_End(OWD): This function ends the timer for measuring OWD and calculates the total time of OWD. The OWD parameter is used to indicate whether the user wants to measure OWD.
interval(number_of_data): This function calculates the time interval based on the number of data sent and the reference interval.
isserver(args): This function checks whether the user wants to run the program as a server or not.
isclient(args): This function checks whether the user wants to run the program as a client or not.
client(args): This function implements the client side of the program. It connects to the server, sends data to the server, and calculates the OWD.
server(args): This function implements the server side of the program. It listens for incoming connections from clients, receives data from clients, and calculates the throughput, jitter, and OWD.
main(): This function is the main function of the program. It calls the other functions based on the user's input.
How to use
To run the program, use the following command:


python server-client.py --a <IP address> --p <port number> --i <reference interval> --s/--c --l <data size> --t <time duration>

<IP address>: The IP address of the server/client. Default value is 127.0.0.1.
<port number>: The port number of the server/client. Default value is 65432.
<reference interval>: The reference interval for sending data. Default value is 1 second.
--s: Run the program as a server.
--c: Run the program as a client.
<data size>: The size of the data to be sent. Default value is 1024.
<time duration>: The duration of the program

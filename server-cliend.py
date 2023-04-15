######################## Server - Client ############################
####### Aimilios Psathas 
####### email: epsathas93@gmail.com


####### Libraries #######

import socket            
import time
import argparse

####### functions ########
def input_argument():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", help = " IP address ", type = str ,default = "127.0.0.1") 
    parser.add_argument("--p", help = " Port ", type = int ,default = "65432") 
    parser.add_argument("--i", help = " Reference interval ",type = int ,default = 1)
    parser.add_argument("--s", help = " Server ", action = "store_true")
    parser.add_argument("--c", help = " Client ",action = "store_true")
    parser.add_argument("--l", help = " Size of Data send ", type = int ,default = "1024") 
    parser.add_argument("--t", help = " Seconds ", type = int ,default = "1")
    args = parser.parse_args()

def throughput_Start(thr):
    global start
    global end
    global total_data_send
    if (thr is True):
        start = time.time()

def throughput_End(thr):
    per_sec = args.i
    if (thr is True):
        end = time.time()
        print("Throughtput is  %f Bytes per %d sec"  % ( (total_data_send/(end - start)), per_sec) )
    
    
def jitter_Start(jit):
    global jitter_arr
    global jitter_count
    global t1
    if (jit is True):
        t1= time.time()
        jitter_arr.append(time.time()- t1)
        jitter_count = jitter_count + 1

def jitter_End(jit):
    global jitter_arr
    global jitter_count
    if(jit is True):
        print("Mean time of jitter is : %f nanosec " % (1000000*(sum(jitter_arr)/jitter_count)))
    
def OWD_Start(OWD):

    global start2
    if (OWD is True):
        start2 = time.time()
        
def OWD_End(OWD):
    if(OWD is True):
        end2 = time.time()
        print("Total time OF OWD : %f nanosec" % (1000000*(end2 - start2)/2))
    
def interval(number_of_data):
    interv = args.i
    return1 = number_of_data/interv ## ta kanw per i
    return return1


def isserver(args):
    if args.s is True:
        return True
    else:
        return False        

def isclient(args):
    if args.c is True:
        return True
    else:
        return False    

def client(args):       ###### client #######
    l = args.l
    host = args.a
    port = args.p
    k = args.t
    j=-1
    data = l*'a'  
    tx = time.time() + k
    ending_package = '\0' 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
        s.connect((host, port))  
        OWD_Start(bool_OWD)
        received_data = s.recv(l).decode()
        if received_data:
            OWD_End(bool_OWD)
            while ( time.time() < tx):
                s.sendall(( data ).encode())  # se bites
                j = j + 1 
            time.sleep(0.02)
            s.sendall((ending_package).encode())

def server(args):    ##### server ######
    global bool_jit
    l = args.l
    s = socket.socket()        
    print ("Socket successfully created")
    host = args.a
    port = args.p         
    s.bind((host, port))        
    print ("socket binded to %s" %(port))
    s.listen(5)    
    print ("socket is listening")  
    global total_data_send    
    while True:
        c, addr = s.accept()   
        print ('Got connection from', addr )
        c.send(("You are accepted ").encode())   ## stelenxw oti sunde8ike kai eimai etoimos na ton dekto
        num_of_packs_send = 0
        data=[]
        throughput_Start(bool_thr)
        while ("\0" not in data):
                jitter_Start(bool_jit)

                data = c.recv(l).decode()
                num_of_packs_send = num_of_packs_send + 1
        total_data_send = num_of_packs_send * l    #  esteile l*number_of_packs data 
        throughput_End(bool_thr)

        jitter_End(bool_jit)              
        c.close()

def main():
    global jitter_arr
    global jitter_count
    jitter_arr = []
    jitter_count = 0 
    global bool_jit
    global bool_thr
    global bool_OWD
    bool_jit = False
    bool_thr = False
    bool_OWD = False
    input_argument()
    isserver(args)
    print(args)

   ### kanw elenxo 
    if (isserver(args) is True) and (isclient(args) is False) :

        bool_jit = input("Do you want to do Jitter metric? Type True or False: ")
        if bool_jit == "True":
            bool_jit = True
        else:
            bool_jit = False
        bool_thr = input("Do you want to do Throughput metric? Type True or False: ")
        if bool_thr == "True":
            bool_thr = True
        else:
            bool_thr = False
        print("Server running")
        server(args)

    elif (isserver(args) is False) and (isclient(args) is True ):
        bool_OWD = input("Do you want to do OWD metric? Type True or False: ")
        if bool_OWD == "True":
            bool_OWD = True
        else:
            bool_thr = False
        print("Server running")
        print("Client running")
        client(args)
    else :
        print("You called neither of them")
####### main program ########
if __name__ == "__main__" :
    main()
#  Eric Feng

#  This is the actual testing file for the serialization logic. Tests health, order,
#  and response.    
#  Here our custom message format comprises a sequence number, a timestamp, a name,
#  and a data buffer of several uint32 numbers (whose value is not relevant to us) 

# The different packages we need in this Python driver code
import os
import sys
import time  # needed for timing measurements and sleep

import random  # random number generator
import argparse  # argument parser

## the following are our files
from health_msg import HealthMessage  # our health message in native format
from order_msg import OrderMessage    # our order message in native format
from response_msg import ResponseMessage   # our response message in native format

import serialize as sz  # this is from the file serialize.py in the same directory

##################################
#        Driver program
##################################

def driver (type, contents, code):

    print ("Driver program: Type = {}, Contents = {} Code (only for Response) = {}".format (type, contents, code))

    # Key: 0 for Health, 1 for Order, 2 for Response
    if type == 0:
        hm = HealthMessage()   # create this once and reuse it for send/receive
        
    elif type == 1:
        om = OrderMessage()

    elif type == 2:
        rm = ResponseMessage()  

    cm = rm

  #  cm.seq_num = random.randint (1, 100)  # Just temporary - I haven't set up the loop yet
    cm.ts = time.time()
    cm.type = type
    cm.contents = contents
    
          
    # if there is code, assign value 
    if type != 0:
        cm.code = code


    print ("-----Iteration: {} contents of message before serializing ----------".format (cm.contents))

    cm.dump ()
        


    # here we are calling our serialize method passing it
    # the iteration number, the topic identifier, and length.
    # The underlying method creates some dummy data, fills
    # up the data structure and serializes it into the buffer
    print ("serialize the message")
    start_time = time.time ()
    buf = sz.serialize (cm)
    end_time = time.time ()
    print ("Serialization took {} secs".format (end_time-start_time))

    # now deserialize and see if it is printing the right thing
    print ("deserialize the message")
    start_time = time.time ()
    cm = sz.deserialize (buf)
    end_time = time.time ()
    print ("Deserialization took {} secs".format (end_time-start_time))

    print ("------ contents of message after deserializing ----------")
    cm.dump ()

    # sleep a while before we send the next serialization so it is not
    # extremely fast
    time.sleep (0.050)  # 50 msec


##################################
# Command line parsing
##################################
def parseCmdLineArgs ():
    # parse the command line
    parser = argparse.ArgumentParser ()

    # add optional arguments
    parser.add_argument ("-t", "--type", default=2, help="The type of message")
    parser.add_argument ("-c", "--contents", default=1, help="The contents of the message")
    parser.add_argument ("-x", "--code", default=0, help="Code of message (only for Response)")

    # parse the args
    args = parser.parse_args ()

    return args
    
#------------------------------------------
# main function
def main ():
    """ Main program """

    print("Demo program for Flatbuffer serialization/deserialization")

    # first parse the command line args
    parsed_args = parseCmdLineArgs ()
    
   # start the driver code
    driver (parsed_args.type, parsed_args.contents, parsed_args.code)

#----------------------------------------------
if __name__ == '__main__':
    main ()

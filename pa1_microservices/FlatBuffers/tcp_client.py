# Sample code for CS4283-5283
# Vanderbilt University
# Instructor: Aniruddha Gokhale
# Created: Fall 2022
# 
# Code taken from ZeroMQ's sample code for the HelloWorld
# program, but modified to use REQ-REP sockets to showcase
# TCP. Plus, added other decorations like comments, print statements,
# argument parsing, etc.
#
# ZMQ is also offering a new CLIENT-SERVER pair of ZMQ sockets but
# these are still in draft form and are not properly supported. If you
# want to try, just replace REQ by CLIENT here (and correspondingly, in
# the tcp_server.py, replace REP by SERVER)
#
# Note: my default indentation is now set to 2 (in other snippets, it
# used to be 4)

# import the needed packages
import sys    # for system exception
import time   # for sleep
import argparse # for argument parsing
import zmq    # this package must be imported for ZMQ to work
import random

from master_msg import Master, Types
import health_msg
import order_msg
import response_msg

import serialize as sz


##################################
# Driver program
##################################
def driver (h_address: str, g_address: str, h_port: int, g_port: int):
  try:
    print ("Obtain the ZMQ context")
    context = zmq.Context ()
  except zmq.ZMQError as err:
    print ("ZeroMQ Error: {}".format (err))
    return
  except:
    print ("Some exception occurred getting context {}".format (sys.exc_info()[0]))
    return

  try:
    # The socket concept in ZMQ is far more advanced than the traditional socket in
    # networking. Each socket we obtain from the context object must be of a certain
    # type. For TCP, we will use the REQ socket type (many other pairs are supported)
    # and this is to be used on the client side.
    hsocket = context.socket (zmq.REQ)
    gsocket = context.socket (zmq.REQ)
  except zmq.ZMQError as err:
    print ("ZeroMQ Error obtaining context: {}".format (err))
    return
  except:
    print ("Some exception occurred getting REQ socket {}".format (sys.exc_info()[0]))
    return

  try:
    # as in a traditional socket, tell the system what IP addr and port are we
    # going to connect to. Here, we are using TCP sockets.
    health_string = "tcp://" + h_address + ":" + str (h_port)
    grocery_string = "tcp://" + g_address + ":" + str (g_port)

    hsocket.connect (health_string)
    gsocket.connect (grocery_string)
  except zmq.ZMQError as err:
    print ("ZeroMQ Error connecting REQ socket: {}".format (err))
    hsocket.close ()
    gsocket.close ()
    return
  except:
    print ("Some exception occurred connecting REQ socket {}".format (sys.exc_info()[0]))
    hsocket.close ()
    gsocket.close()
    return

  #  Wait for next request from client
  print ("Send a response message from the client")

  try:
    
    # create health message
    hm = Master()
    hm.ts = time.time()
    hm.type = Types.HEALTH

    health_body = health_msg.HealthBody()
    health_body.dispenser = health_msg.DispenserOptions.OPTIMAL
    health_body.icemaker = 90
    health_body.lightbulb = health_msg.LightStatus.GOOD
    health_body.fridge_temp = 37
    health_body.freezer_temp = 0
    health_body.sensor_status = health_msg.SensorStatus.GOOD
    health_body.humidity = .56
    health_body.door_openings = 3

    hm.body = health_body


    # create grocery/order message
    gm = Master()
    gm.ts = time.time()
    gm.type = Types.ORDER

    order_body = order_msg.OrderBody()
    order_body_veggies = order_msg.VeggieOrder()
    order_body_veggies.tomato = 1.5
    order_body_veggies.cucumber = 2.0
    order_body_veggies.eggplant = 3.5
    order_body_veggies.broccoli = 4.0
    order_body_veggies.carrot = 5.0
    order_body_veggies.onion = 6.0
    order_body.veggies = order_body_veggies

    order_body_drinks = order_msg.CansAndBottles()
    order_body_drinks_cans = order_msg.CanOrder()
    order_body_drinks_cans.coke = 2
    order_body_drinks_cans.pepsi = 6
    order_body_drinks_cans.coors = 24
    order_body_drinks.cans = order_body_drinks_cans

    order_body_drinks_bottles = order_msg.BottleOrder()
    order_body_drinks_bottles.sprite = 3
    order_body_drinks_bottles.rootbeer = 1
    order_body_drinks_bottles.fanta = 2
    order_body_drinks.bottles = order_body_drinks_bottles
    order_body.drinks = order_body_drinks

    order_body.milk = [order_msg.MilkType.Almond, 2.0]
    order_body.bread = [order_msg.BreadType.Sourdough, 1]
    order_body.meat = [order_msg.MeatType.Chicken, 2.5]
    
    gm.body = order_body
 

    print ("serializing message of type {}".format (hm.type))
    print ("serializing message of type {}".format (gm.type))

    hm.dump()
    gm.dump()

    start_time = time.time()
    hsocket.send_serialized(hm, sz.serialize_to_frames)
    end_time = time.time()

    print("Time to serialize - Response:", end_time - start_time)

    start_time = time.time()
    gsocket.send_serialized(gm, sz.serialize_to_frames)
    end_time = time.time()

    print("Time to serialize - Health:", end_time - start_time)


    try:
      serialized = sz.serialize_to_frames(hm)
      deser = sz.deserialize_from_frames(serialized)
      print("Deserialized response msg: \n{}".format(deser))

      serialized = sz.serialize_to_frames(gm)
      deser = sz.deserialize_from_frames(serialized)
      print("Deserialized health msg: \n{}".format(deser))
    except:
      raise

    

  except zmq.ZMQError as err:
    print ("ZeroMQ Error sending: {}".format (err))
    hsocket.close ()
    return
  except:
    print ("(1) Some exception occurred receiving/sending {}".format (sys.exc_info()))
    gsocket.close ()
    return
  

  try:
    # receive a reply
    print ("Waiting to receive")
    h_message = hsocket.recv ()
    h_deser_msg = sz.deserialize(h_message)
    print("received response from server: \n{}".format(h_deser_msg))

    g_message = gsocket.recv ()
    g_deser_msg = sz.deserialize(g_message)
    print("received response from server: \n{}".format(g_deser_msg))

    return
  
  except zmq.ZMQError as err:
    print ("ZeroMQ Error receiving: {}".format (err))
    hsocket.close ()
    gsocket.close ()
    return
  except:
    print ("(2) Some exception occurred receiving/sending {}".format (sys.exc_info()))
    hsocket.close ()
    gsocket.close ()
    return
  



##################################
# Command line parsing
##################################
def parseCmdLineArgs ():
  # parse the command line
  parser = argparse.ArgumentParser ()

  # add optional arguments
  parser.add_argument ("-a", "--haddr", default="127.0.0.1", help="IP Address to connect to (default: localhost i.e., 127.0.0.1)")
  parser.add_argument ("-b", "--gaddr", default="127.0.0.1", help="GROCERY SERVER IP Address to connect to (default: localhost i.e., 127.0.0.1)")
  parser.add_argument ("-p", "--hport", type=int, default=5577, help="Port that server is listening on (default: 5577)")
  parser.add_argument ("-g", "--gport", type=int, default=5578, help="Port where the grocery server part of the peer listens and client side connects to (default: 5578)")
    
  args = parser.parse_args ()

  return args
    
#------------------------------------------
# main function
def main ():
  """ Main program """

  print("Demo program for TCP Client with ZeroMQ")

  # first parse the command line args
  parsed = parseCmdLineArgs ()
    
  # start the driver code
  driver (h_address=parsed.haddr, g_address=parsed.gaddr, h_port=parsed.hport, g_port=parsed.gport)

#----------------------------------------------
if __name__ == '__main__':
  # here we just print the version numbers
  print("Current libzmq version is %s" % zmq.zmq_version())
  print("Current pyzmq version is %s" % zmq.pyzmq_version())

  main ()

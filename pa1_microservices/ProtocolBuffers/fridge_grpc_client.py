#  Author: Aniruddha Gokhale
#  Created: Fall 2023
#
#  Purpose: demonstrate serialization of a user-defined data structure using
#  Protocol Buffers combined with gRPC. Note that here we
#  are more interested in how a serialized packet gets sent over the network
#  and retrieved. To that end, we really don't care even if the client and
#  server were both on the same machine or remote to each other.

# This one implements the client functionality
import os
import sys
import time  # needed for timing measurements and sleep

import random  # random number generator
import argparse  # argument parser

import logging

import grpc   # for gRPC

# import generated packages
import schema_pb2 as spb
import schema_pb2_grpc as spb_grpc

##################################
#        Driver program
##################################

def driver (h_address: str, g_address: str, h_port: int, g_port: int, iters: int):

  print ("Driver program will try sending {} messages of each type health server at {} and grocery server at {}".format (iters, h_address, g_address))

  # first obtain a peer and initialize it
  print ("Driver program: create handle to the client and then run the code")
  try:

    # Use the insecure channel to establish connection with server
    print ("Instantiate insecure channel (health)")
    health_channel = grpc.insecure_channel (h_address+ ":" + str (h_port))
    print ("Instantiate insecure channel (grocery)")
    grocery_channel = grpc.insecure_channel (g_address+ ":" + str (g_port))

    print ("Obtain a proxy object to the health server")
    h_stub = spb_grpc.DummyServiceStub (health_channel)
    print ("Obtain a proxy object to the grocery server")
    g_stub = spb_grpc.DummyServiceStub (grocery_channel)

    # now send the serialized custom message for the number of desired iterations
    print ("Allocate the Request object that we will then populate in every iteration")
    health_req = spb.Master()
    grocery_req = spb.Master()

    for it in range(iters):
      health_req.ts = time.time()  # current time
      health_req.type = spb.MsgType.HealthType
      # Create a Health message
      health_message = spb.Health()
      # Set the fields of the Health message
      health_message.dispenser = spb.DispenserStatus.OPTIMAL
      health_message.icemaker = 89  # Set to your desired value
      health_message.lightbulb = spb.LightbulbStatus.LIGHT_GOOD
      health_message.fridge_temp = 35  # Set to your desired value
      health_message.freezer_temp = -10  # Set to your desired value
      health_message.sensor_status = spb.SensorStatus.SENSOR_GOOD
      health_message.humidity = 50.0  # Set to your desired value
      health_message.door_openings = 5  # Set to your desired value
      health_req.healthBody.CopyFrom(health_message)

      grocery_req.type = spb.MsgType.OrderType
      order_message = get_default_order_msg()
      grocery_req.orderBody.CopyFrom(order_message)

      print("-----Iteration: {} contents of message before sending\nHEALTH:\n{}\nGROCERY:\n{} ----------".format(it, health_req, grocery_req))
      # now let the client send the message to its server part
      print("client sending the serialized message (health)")
      start_time = time.time()
      resp = h_stub.method(health_req)
      print("received response: \n{}".format(resp))
      end_time = time.time()
      print("sending/receiving took {} secs".format(end_time - start_time))

      print("client sending the serialized message (grocery)")
      start_time = time.time()
      resp = g_stub.method(grocery_req)
      print("received response: \n{}".format(resp))
      end_time = time.time()
      print("sending/receiving took {} secs".format(end_time - start_time))

      # sleep a while before we send the next serialization so it is not extremely fast
      time.sleep(0.050)  # 50 msec

  except:
    return
  
  

  
##################################
# Command line parsing
##################################
def parseCmdLineArgs ():
    # parse the command line
    parser = argparse.ArgumentParser ()

    # add optional arguments
    parser.add_argument ("-i", "--iters", type=int, default=1, help="Number of iterations to run (default: 1)")
    parser.add_argument ("-p", "--hport", type=int, default=5577, help="Port where the health server part of the peer listens and client side connects to (default: 5577)")
    parser.add_argument ("-g", "--gport", type=int, default=5578, help="Port where the grocery server part of the peer listens and client side connects to (default: 5578)")
    parser.add_argument ("-a", "--haddr", default="127.0.0.1", help="HEALTH SERVER IP Address to connect to (default: localhost i.e., 127.0.0.1)")
    parser.add_argument ("-b", "--gaddr", default="127.0.0.1", help="GROCERY SERVER IP Address to connect to (default: localhost i.e., 127.0.0.1)")
    
    # parse the args
    args = parser.parse_args ()

    return args

def get_default_order_msg() -> spb.Order:
     '''helper to assemble the complex order message structure'''
     # Create an Order message
     order_message = spb.Order()

     # Populate the VeggieOrder message
     veggie_order = spb.VeggieOrder()
     veggie_order.tomato = 2.0
     veggie_order.cucumber = 1.5
     veggie_order.eggplant = 1.0
     veggie_order.broccoli = 3.0
     veggie_order.carrot = 4.0
     veggie_order.onion = 2.5

     # Populate the CansAndBottles message
     cans_and_bottles = spb.CansAndBottles()
     cans_and_bottles.cans.coke = 12
     cans_and_bottles.cans.pepsi = 10
     cans_and_bottles.cans.coors = 6
     cans_and_bottles.bottles.sprite = 8
     cans_and_bottles.bottles.rootbeer = 6
     cans_and_bottles.bottles.fanta = 5 
 
     # Populate the list of Milk messages
     milk_messages = [
        spb.Milk(type=spb.Milk.OnePercent, quantity=1.0),
        spb.Milk(type=spb.Milk.TwoPercent, quantity=2.0),
        spb.Milk(type=spb.Milk.FatFree, quantity=0.5),
     ]

     # Populate the list of Bread messages
     bread_messages = [
        spb.Bread(type=spb.Bread.WholeWheat, quantity=3),
        spb.Bread(type=spb.Bread.Rye, quantity=2),
        spb.Bread(type=spb.Bread.White, quantity=4),
     ]

     # Populate the list of Meat messages
     meat_messages = [
        spb.Meat(type=spb.Meat.GroundBeef, quantity=2.5),
        spb.Meat(type=spb.Meat.Chicken, quantity=3.0),
        spb.Meat(type=spb.Meat.Steak, quantity=1.5),
     ]

     # Set the VeggieOrder, CansAndBottles, Milk, Bread, and Meat in the Order message
     order_message.veggies.CopyFrom(veggie_order)
     order_message.drinks.CopyFrom(cans_and_bottles)
     order_message.milk.extend(milk_messages)
     order_message.bread.extend(bread_messages)
     order_message.meat.extend(meat_messages)

     return order_message

def get_default_health_msg():
  # Create a Health message
  health_message = spb.Health()
  # Set the fields of the Health message
  health_message.dispenser = spb.DispenserStatus.OPTIMAL
  health_message.icemaker = 89  # Set to your desired value
  health_message.lightbulb = spb.LightbulbStatus.LIGHT_GOOD
  health_message.fridge_temp = 35  # Set to your desired value
  health_message.freezer_temp = -10  # Set to your desired value
  health_message.sensor_status = spb.SensorStatus.SENSOR_GOOD
  health_message.humidity = 50.0  # Set to your desired value
  health_message.door_openings = 5  # Set to your desired value
#------------------------------------------
# main function
def main ():
  """ Main program """

  print("Client program for proto+grpc")

  # first parse the command line args
  parsed = parseCmdLineArgs ()
    
  # start the driver code
  driver (h_address=parsed.haddr, g_address=parsed.gaddr, h_port=parsed.hport, g_port=parsed.gport, iters=parsed.iters)

#----------------------------------------------
if __name__ == '__main__':
    main ()

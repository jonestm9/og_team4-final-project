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
# want to try, just replace REP by SERVER here (and correspondingly, in
# the tcp_client.py, replace REQ by CLIENT)
#
# Note: my default indentation is now set to 2 (in other snippets, it
# used to be 4)

# import the needed packages
import sys    # for system exception
import time   # for sleep
import argparse # for argument parsing
import zmq
from master_msg import Master, Types
import health_msg
import response_msg    # this package must be imported for ZMQ to work

import serialize as sz

##################################
# Driver program
##################################
def driver (intf, h_port, g_port):
  try:
    # every ZMQ session requires a context
    print ("Obtain the ZMQ context")
    context = zmq.Context ()   # returns a singleton object
  except zmq.ZMQError as err:
    print ("ZeroMQ Error obtaining context: {}".format (err))
    return
  except:
    print ("Some exception occurred getting context {}".format (sys.exc_info()[0]))
    return

  try:
    # The socket concept in ZMQ is far more advanced than the traditional socket in
    # networking. Each socket we obtain from the context object must be of a certain
    # type. For TCP, we will use REP for server side (many other pairs are supported
    # in ZMQ for tcp.
    print ("Obtain the REP type socket")
    hsocket = context.socket (zmq.REP)
    gsocket = context.socket (zmq.REP)
  except zmq.ZMQError as err:
    print ("ZeroMQ Error obtaining REP socket: {}".format (err))
    return
  except:
    print ("Some exception occurred getting REP socket {}".format (sys.exc_info()[0]))
    return

  try:
    # as in a traditional socket, tell the system what port are we going to listen on
    # Moreover, tell it which protocol we are going to use, and which network
    # interface we are going to listen for incoming requests. This is TCP.
    h_string = "tcp://" + intf + ":" + str (h_port)
    g_string = "tcp://" + intf + ":" + str (g_port)
    print ("TCP server will be binding on {}".format (h_string))
    hsocket.bind(h_string)
    gsocket.bind(g_string)
  except zmq.ZMQError as err:
    print ("ZeroMQ Error binding REP socket: {}".format (err))
    hsocket.close ()
    gsocket.close ()
    return
  except:
    print ("Some exception occurred binding REP socket {}".format (sys.exc_info()[0]))
    hsocket.close ()
    gsocket.close ()
    return

  # since we are a server, we service incoming clients forever
  print ("Server now waiting to receive something")
  while True:
    try:
      #  Wait for next request from client
      h_message = hsocket.recv()
      print("Received serialized request: %s" % h_message)
      deser_msg = sz.deserialize(h_message)
      print("deserialized message: \n{}".format(deser_msg))

      #  Wait for next request from client
      g_message = gsocket.recv()
      print("Received serialized request: %s" % g_message)
      deser_msg = sz.deserialize(g_message)
      print("deserialized message: \n{}".format(deser_msg))

    except zmq.ZMQError as err:
      print ("ZeroMQ Error receiving: {}".format (err))
      hsocket.close ()
      gsocket.close ()
      return
    except:
      print ("Some exception occurred receiving/sending {}".format (sys.exc_info()[0]))
      hsocket.close ()
      gsocket.close ()
      return


    #  Do some 'work'. In this case we just sleep.
    time.sleep (1)

    try:
      #  Send reply back to client
      print ("Send response")
      
      # create response message (native)
      rm = Master()
      rm.ts = time.time()
      rm.type = Types.RESPONSE

      response_body = response_msg.ResponseBody()
      response_body.code = response_msg.RequestStatus.OK
      response_body.contents = response_msg.ResponseStatus.YOU_ARE_HEALTHY

      rm.body = response_body


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


      print ("serializing message of type {}".format (rm.type))
      hsocket.send_serialized(rm, sz.serialize_to_frames)

      print ("serializing message of type {}".format (hm.type))
      gsocket.send_serialized(hm, sz.serialize_to_frames)


      return
    except zmq.ZMQError as err:
      print ("ZeroMQ Error sending: {}".format (err))
      hsocket.close ()
      gsocket.close ()
      return
    except:
      print ("Some exception occurred receiving/sending {}".format (sys.exc_info()[0]))
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
  parser.add_argument ("-i", "--intf", default="*", help="Interface to bind to (default: *)")
  parser.add_argument ("-p", "--hport", type=int, default=5577, help="Port to bind to (default: 5577)")
  parser.add_argument ("-g", "--gport", type=int, default=5578, help="Port to bind to (default: 5578)")

  args = parser.parse_args ()

  return args
    
#------------------------------------------
# main function
def main ():
  """ Main program """

  print("Demo program for TCP Server with ZeroMQ")

  # first parse the command line args
  parsed = parseCmdLineArgs ()
    
  # start the driver code
  driver (intf=parsed.intf, h_port=parsed.hport, g_port=parsed.gport)

#----------------------------------------------
if __name__ == '__main__':
  # here we just print the version numbers
  print("Current libzmq version is %s" % zmq.zmq_version())
  print("Current pyzmq version is %s" % zmq.pyzmq_version())

  main ()

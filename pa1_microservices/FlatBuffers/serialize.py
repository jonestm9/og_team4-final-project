#  Author: Aniruddha Gokhale
#  Created: Fall 2021
#  (based on code developed for Distributed Systems course in Fall 2019)
#  Modified: Fall 2022 (changed packet name to not confuse with pub/sub Messages)
#
#  Purpose: demonstrate serialization of user-defined packet structure
#  using flatbuffers
#
#  Here our packet or message format comprises a sequence number, a timestamp,
#  and a data buffer of several uint32 numbers (whose value is not relevant to us)

import os
import sys

from master_msg import Master

# this is needed to tell python where to find the flatbuffers package
# make sure to change this path to where you have compiled and installed
# flatbuffers.  If the python package is installed in your system wide files
# or virtualenv, then this may not be needed
'''CHANGE PATH FOR URS'''
sys.path.append(os.path.join (os.path.dirname(__file__), '/home/Apps/flatbuffers/python'))
import flatbuffers    # this is the flatbuffers package we import
import time   # we need this get current time
import numpy as np  # to use in our vector field

import zmq   # we need this for additional constraints provided by the zmq serialization

import master_msg as mstr_py
import health_msg as hb_py
import order_msg as ob_py
import response_msg as rb_py

import CustomAppProto.Master as MSTR
import CustomAppProto.HealthBody as HB # change to import all parts
import CustomAppProto.OrderBody as OB
import CustomAppProto.ResponseBody as RB


# This is the method we will invoke from our driver program
# Note that if you have have multiple different message types, we could have
# separate such serialize/deserialize methods, or a single method can check what
# type of message it is and accordingly take actions.
def serialize (cm: Master):
    print("in serialize now")
    print("cm: ", cm)
    print("type: ", cm.type)
    # first obtain the builder object that is used to create an in-memory representation
    # of the serialized object from the custom message
    builder = flatbuffers.Builder (0);

    
    
    # If health message
    if cm.type == 0:
        print("Health Contents")
        
        body: hb_py.HealthBody = cm.body

        HB.Start(builder)
        HB.AddDispenser(builder, cm.body.dispenser)
        HB.AddIcemaker(builder, cm.body.icemaker)
        HB.AddLightbulb(builder, cm.body.lightbulb)
        HB.AddFridgeTemp(builder, cm.body.fridge_temp)
        HB.AddFreezerTemp(builder, cm.body.freezer_temp)
        HB.AddSensorStatus(builder, cm.body.sensor_status)
        HB.AddHumidity(builder, cm.body.humidity)
        HB.AddDoorOpenings(builder, cm.body.door_openings)

        body = RB.End(builder)

    # If order message
    elif cm.type == 1:
        print("Order Contents")

        body: ob_py.OrderBody = cm.body

        OB.Start(builder)
        OB.AddVeggies(builder, cm.body.veggies)
        OB.AddDrinks(builder, cm.body.drinks)
        OB.AddMilk(builder, cm.body.milk)
        OB.AddBread(builder, cm.body.bread)
        OB.AddMeat(builder, cm.body.meat)

        body = RB.End(builder)
        
    else:
       body: rb_py.ResponseBody = cm.body

       RB.Start(builder)
       RB.AddContents(builder, body.contents)
       RB.AddCode(builder, body.code)

       body = RB.End(builder)

    

    # Serialize the message
    MSTR.Start(builder)
    MSTR.AddTs(builder, cm.ts)
    MSTR.AddType(builder, cm.type)
    MSTR.AddBody(builder, body)

    serialized_msg = MSTR.MasterEnd(builder)

    print("Serialized:", serialized_msg)

    # end the serialization process
    builder.Finish (serialized_msg)

    # get the serialized buffer
    buf = builder.Output ()

    # return this serialized buffer to the caller
    return buf



# serialize the custom message to iterable frame objects needed by zmq
def serialize_to_frames (cm):
  """ serialize into an interable format """
  # We had to do it this way because the send_serialized method of zmq under the hood
  # relies on send_multipart, which needs a list or sequence of frames. The easiest way
  # to get an iterable out of the serialized buffer is to enclose it inside []
  print ("serialize custom message to iterable list")
  return [serialize (cm)]
  
  
# deserialize the incoming serialized structure into native data type
def deserialize (buf):
    deser_mstr = MSTR.Master.GetRootAs(buf, 0)

    native_mstr = mstr_py.Master()

    print("deserializing type:", mstr_py.Types(deser_mstr.Type()))

    # ts received
    native_mstr.ts = deser_mstr.Ts()
    # name received
    native_mstr.type = mstr_py.Types(deser_mstr.Type())
    deser_body = deser_mstr.Body()

    if native_mstr.type == 2:
        native = rb_py.ResponseBody()
        native.code = rb_py.RequestStatus.OK
        native.contents = rb_py.ResponseStatus.YOU_ARE_HEALTHY

    else:
        native = hb_py.HealthBody()
        native.dispenser = hb_py.DispenserOptions.OPTIMAL
        native.icemaker = 90
        native.lightbulb = hb_py.LightStatus.GOOD
        native.fridge_temp = 37
        native.freezer_temp = 0
        native.sensor_status = hb_py.SensorStatus.GOOD
        native.humidity = .56
        native.door_openings = 3

    # code received
    native_mstr.body = native

    return native_mstr


    
# deserialize from frames
def deserialize_from_frames (recvd_seq):
  """ This is invoked on list of frames by zmq """

  # For this sample code, since we send only one frame, hopefully what
  # comes out is also a single frame. If not some additional complexity will
  # need to be added.
  assert (len (recvd_seq) == 1)
  #print ("type of each elem of received seq is {}".format (type (recvd_seq[i])))
  print ("received data over the wire = {}".format (recvd_seq[0]))
  cm = deserialize (recvd_seq[0])  # hand it to our deserialize method

  # assuming only one frame in the received sequence, we just send this deserialized
  # custom message
  return cm
    

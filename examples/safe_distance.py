import jpype
# import jpype.imports

import time
import math
from jvm_setup import JVMSetup

class SafeDistance():
    def __init__(self):
        JVMSetup.initializeJVM()
        self.monitor = jpype.JClass("safe_distance.TraceMonitor") 
        self.file = open("SafeDistanceResults.txt","w")
    
    def send_data(self, event, world, ego_actor):
        jpype.attachThreadToJVM()
        my_vehicle = ego_actor
        other_vehicle = world.get_actor(event.other_actor.id)
        my_velocity = my_vehicle.get_velocity()
        my_speed = math.sqrt(my_velocity.x**2 + my_velocity.y**2 + my_velocity.z**2) # in kph
        other_velocity = other_vehicle.get_velocity()
        other_speed = math.sqrt(other_velocity.x**2 + other_velocity.y**2 + other_velocity.z**2) # in kph
        # subtract 2 meters (distance from center of ego vehicle to leading car)
        distance = event.distance-2.0
        message = "detectLeadingVehicle,{},{},{}".format(my_speed,other_speed,distance)
        result = self.monitor.eval(message)
        if not result:
            print("Safe distance property violated on event {}".format(message))

        self.file.write("{},{}\n".format(message,str(result)))

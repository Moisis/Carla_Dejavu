import jpype
# import jpype.imports

import time
import math
from jvm_setup import JVMSetup

class SpeedLimit():
    def __init__(self):
        JVMSetup.initializeJVM()
        self.monitor = jpype.JClass("speed_limit.TraceMonitor")
        self.file = open("SpeedLimitResults.txt","w")
    
    def send_data(self, ego_actor):
        jpype.attachThreadToJVM()
        # data = [["VehicleSpeedChanged", self.uid, ego_speed, self.carla_actor.get_speed_limit()]]
        my_vehicle = ego_actor
        my_velocity = my_vehicle.get_velocity()
        my_speed = 3.6 * math.sqrt(my_velocity.x**2 + my_velocity.y**2 + my_velocity.z**2)
        message = "SpeedChanged,{},{}".format(int(my_speed),int(my_vehicle.get_speed_limit()))
        result = self.monitor.eval(message)
        if not result:
            print("Speed limit property violated on event {}".format(message))

        self.file.write("{},{}\n".format(message,str(result)))

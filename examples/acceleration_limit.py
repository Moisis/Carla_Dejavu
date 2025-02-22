import jpype
import time
import math
from jvm_setup import JVMSetup

class AccelerationLimit():
    def __init__(self):
        JVMSetup.initializeJVM()
        self.monitor = jpype.JClass("acceleration_limit.TraceMonitor")
        self.file = open("AccelerationLimitResults.txt","w")
    
    def send_data(self, ego_actor):
        jpype.attachThreadToJVM()
        my_vehicle = ego_actor
        my_acceleration = my_vehicle.get_acceleration()
        my_acceleration_limit = "20"
        
        # Calculate acceleration magnitude
        acceleration_magnitude = math.sqrt(my_acceleration.x**2 + my_acceleration.y**2 + my_acceleration.z**2)
        
        message = "AccelerationChanged,{},{}".format(int(acceleration_magnitude), int(my_acceleration_limit))
        result = self.monitor.eval(message)
        if not result:
            print("Acceleration limit property violated on event {}".format(message))

        self.file.write("{},{}\n".format(message,str(result)))

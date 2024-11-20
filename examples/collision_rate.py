import jpype
# import jpype.imports

import time
import math
from jvm_setup import JVMSetup

class CollisionRate():
    def __init__(self):
        JVMSetup.initializeJVM()
        self.monitor = jpype.JClass("collision_rate.TraceMonitor")
        self.file = open("CollisionRateResults.txt","w")
    
    def send_data(self, collision_value, total_distance):
        jpype.attachThreadToJVM()
        # collide, collision status (1 for collision, 0 for no collision), distance travelled (km)
        total_distance_km = total_distance/1000
        if not total_distance_km:
            return
        message = "collide,{},{}".format(int(collision_value),total_distance_km)
        result = self.monitor.eval(message)
        if not result:
            print("Collision rate property violated on event {}".format(message))

        self.file.write("{},{}\n".format(message,str(result)))




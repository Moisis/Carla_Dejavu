import jpype

class JVMSetup():
    @staticmethod
    def initializeJVM():
        if jpype.isJVMStarted():
            return
        
        jar_path1 = 'tpdejavu.jar'
        jar_path2 = 'SafeDistance.jar'
        jar_path3 = 'SpeedLimit.jar'
        jar_path4 = 'CollisionRate.jar'
        jar_path = "-Djava.class.path={}:{}:{}:{}".format(jar_path1,jar_path2,jar_path3,jar_path4)
        jpype.startJVM(jpype.getDefaultJVMPath(),"-ea", jar_path)
    

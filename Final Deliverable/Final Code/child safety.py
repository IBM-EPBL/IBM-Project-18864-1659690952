import time
import sys
import ibmiotf.application
import ibmiotf.device
import random


#Provide your IBM Watson Device Credentials
organization = "myzpwb"
deviceType = "raspberrypi"
deviceId = "demo123"
authMethod = "token"
authToken = "12345678"





        


try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        #Get Sensor Data from DHT11
        
        name="seetha"
        latitude=13.0480438
        longitude=79.928808
        #latitude=9.9179987
        #longitude=78.0527826

        data = { 'name' : name, 'lat': latitude, 'lon':longitude }
        #print data
        def myOnPublishCallback():
            print ("Published name = %s " % name, "latitude = %s " % latitude, "longitude = %s " % longitude, "to IBM Watson")

        success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
           print("Not connected to IoTF")
        time.sleep(5)
        
        deviceCli.commandCallback = 'myOnPublishCallback'
        

client.disconnect()

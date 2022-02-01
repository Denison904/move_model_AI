from controller import Radar, RadarTarget
from vehicle import Driver
import numpy as np


timestep = int(100.0)
driver = Driver()
driver.setSteeringAngle(0.0)
driver.setCruisingSpeed(10)
# driver.setThrottle(1)
sensor = Radar("Delphi ESR")
sensor.enable(timestep)
print("getMinRange:", sensor.getMinRange())
print("getMaxRange:", sensor.getMaxRange())
while driver.step() != -1:
    # print(sensor.getNumberOfTargets())
    print("Speed: ",driver.getCurrentSpeed())
    if sensor.getNumberOfTargets() > 0:
        print("distance: ", sensor.getTargets()[0].distance)
        if sensor.getTargets()[0].distance < 6 :
            driver.setThrottle(0)
            driver.setBrakeIntensity(1.0)
    else:
        # driver.setThrottle(0.6)
        driver.setBrakeIntensity(0)
  # if x < 2:
    # print("Brake")
    # driver.setBrakeIntensity(1.0)
      
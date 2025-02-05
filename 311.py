# var to stand in for the robot color sensor
eye = "blue"

# method to drive foward
def drivefoward():
    print("foward")
# method to drive right
def turnright():
    print("turn right")
# method to drive left
def turnleft():
    print("left")
'''
drive based on what color the robot sees

'''
def DriveByColor():
    while(true):
        drivefoward()
        if(eye == "green"):
            turnright()
        if(eye == "blue"):
            turnleft()
        if(eye == "red"):
            # stop here

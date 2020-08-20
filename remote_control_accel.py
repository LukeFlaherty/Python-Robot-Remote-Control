import gpiozero
import cwiid

robot = gpiozero.Robot(left=(17,18), right=(27,22))

print("Press and hold the 1 + 2 buttons on your wiimote simultaniously")
wii = cwiid.Wiimote()

print("Connection established")
wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC

while True:
        #reads the x value from the accelerometer and stores it in x
        #the - 95 takes the value it could have from 95-145 to 0-50
        #subtract 25 to ensure the range of date recieved will be between -25+25
        #the robot class treats -values as backwards and + as forwards
        x = (wii.state["acc"][cwiid.X] - 95) - 25
        #reads the y value fromt he accelerometer and stores it in y
        y = (wii.state["acc"][cwiid.Y] - 95) - 25

        #in the rare chance the acc gives values that are not within the -25+25
        #range this controls those errors and round them out
        if x < -25:
                x = -25
        if y < -25:
                y = -25
        if x > 25:
                x = 25
        if y > 25:
                y = 25

        #final x axis value is stored in forward_value
        #divides x by 50 giving a new number between -0.5 and 0.5
        #this is multiplied by 2 to get a value between -1 and 1
        x_value = (float(x) / 50) * 2
        y_value = (float(y) / 50) * 2

        #if the wiimote is tilted by less than 30 percent to either side
        #it will assume you want to move forward/backward
        #that means if wont turn at the "slightest movement" (30 percent)

        #forward/ backward speed is determined by the pitch of your remote
        #pitched all the way forward = robot.value = (1,1) and the robot will
        #accelerate forward

        #if you have your remote tilted all the way to the right your robot
        #will turn in a donut in the right or left direction
        #turns based off the amount your remote is turned
        #if (turn_value < 0.3) and (turn_value > -0.3):
        #        robot.value = (forward_value, forward_value)
        if (forward_value <= -0.2) and (forward_value > -1.0):
                robot.value = (forward_value, forward_value)
        if (forward_value )
        else:
                robot.value = (-turn_value, turn_value)
        if (B button is pressed):
                robot.forward()


        buttons = wii.state["buttons"]
        if (buttons & cwiid.BTN_B):
                 robot.stop()
        if (buttons & cwiid.BTN_A):
                break

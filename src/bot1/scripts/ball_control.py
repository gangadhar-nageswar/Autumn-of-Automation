#!/usr/bin/env python
 

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic
#problem1 - bot may turn first as cx,cy might go down before laser reads 22
import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
import time


## Flaps and Basic Functions ##
pub_fg = rospy.Publisher('/bot1_frontgate_controller/command', Float64, queue_size=10)
pub_lf = rospy.Publisher('/bot1_lf_controller/command', Float64, queue_size=10)
pub_rf = rospy.Publisher('/bot1_rf_controller/command', Float64, queue_size=10)
pub_df = rospy.Publisher('/bot1_diffdrive_controller/cmd_vel', Twist, queue_size=10)

def fg_close():
	t0 = rospy.Time.now().to_sec()
	t1 = t0
	rate2 = rospy.Rate(25)
	while (t1 - t0) < 4:
		pub_fg.publish(5)
		t1 = rospy.Time.now().to_sec()
		rate2.sleep()

def fg_open():
	t0 = rospy.Time.now().to_sec()
	t1 = t0
	rate = rospy.Rate(10)
	while (t1 - t0) < 2:
		pub_fg.publish(-5)
		t1 = rospy.Time.now().to_sec()
		rate.sleep()

def flaps_open(x):
	t0 = rospy.Time.now().to_sec()
	t1 = t0
	rate = rospy.Rate(10)
	while (t1 - t0) < 2:
		pub_lf.publish(x)
		pub_rf.publish(-x)
		t1 = rospy.Time.now().to_sec()
		rate.sleep()

def flaps_close(x):
	t0 = rospy.Time.now().to_sec()
	t1 = t0
	rate3 = rospy.Rate(200)
	while (t1 - t0) < 2:
		pub_lf.publish(-x)
		pub_rf.publish(x)
		t1 = rospy.Time.now().to_sec()
		rate3.sleep()

def rotate(value, t):
	angle = Twist()
	angle.linear.x = 0
	angle.angular.z = value
	t0 = rospy.Time.now().to_sec()
	t1 = t0
	rate = rospy.Rate(10)
	while (t1 - t0) < t:
		pub_df.publish(angle)
		t1 = rospy.Time.now().to_sec()
		rate.sleep()


### ball_control DEFINITION ###

def ball_control(color):
	
	rospy.init_node('ball_controller', anonymous=True)
	
	if color == "red":
		fg_close()
		rotate(0.3, 2)
			
		flaps_open(30)
		time.sleep(0.5)
		flaps_close(1)
			
		rotate(-0.3, 2)

		
	elif color == "green":
		fg_close()
		flaps_open(1)
		time.sleep(1)
		fg_open()
		flaps_close(30)
		time.sleep(1)
		fg_close()
		flaps_close(1)
			

ball_control("green")
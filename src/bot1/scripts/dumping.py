#!/usr/bin/env python


import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
import math
import time

rospy.init_node('distance_calculater', anonymous=True)

## Flaps ##
pub_bg = rospy.Publisher('/bot1_backgate_controller/command', Float64, queue_size=10)
pub_df = rospy.Publisher('/bot1_diffdrive_controller/cmd_vel', Twist, queue_size=10)

def bg_close():
	t0 = rospy.Time.now().to_sec()
	t1 = t0
	rate2 = rospy.Rate(50)
	while (t1 - t0) < 3:
		pub_bg.publish(-5)
		t1 = rospy.Time.now().to_sec()
		rate2.sleep()

def bg_open():
	t0 = rospy.Time.now().to_sec()
	t1 = t0
	while (t1 - t0) < 3:
		pub_bg.publish(-10)
		t1 = rospy.Time.now().to_sec()
		rate.sleep()

def rotate(value, t):
	angle = Twist()
	angle.linear.x = 0
	angle.angular.z = value
	t0 = rospy.Time.now().to_sec()
	t1 = t0
	while (t1 - t0) < t:
		pub_df.publish(angle)
		t1 = rospy.Time.now().to_sec()
		rate.sleep()

def traverse(v,t):
	speed = Twist()
	speed.linear.x = v
	t0 = rospy.Time.now().to_sec()
	t1 = t0
	rate_df = rospy.Rate(50)
	while (t1 - t0) < t:
		pub_df.publish(speed)
		t1 = rospy.Time.now().to_sec()
		rate_df.sleep()

	speed.linear.x = 0
	pub_df.publish(speed)

bg_close()
pi = math.pi


rate = rospy.Rate(30)
 
def dump():
	
	traverse(-0.3, 6)
	rotate(pi/4, 11)
	print(1)
	bg_open()
	traverse(-0.8, 2)
	time.sleep(5)


dump()
	
	
	

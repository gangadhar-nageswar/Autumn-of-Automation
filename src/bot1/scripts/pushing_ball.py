#!/usr/bin/env python


import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
import time

## Code for getting the distance continously ##
rospy.init_node('distance_calculater', anonymous=True)

def callback(msg):
	global distance
	count = 0
	for dist in msg.ranges:
		distance += dist
		count += 1
	distance = distance/count
	
distance = Float32()
distance = 0

## Flaps ##
pub_fg = rospy.Publisher('/bot1_frontgate_controller/command', Float64, queue_size=10)
pub_lf = rospy.Publisher('/bot1_lf_controller/command', Float64, queue_size=10)
pub_rf = rospy.Publisher('/bot1_rf_controller/command', Float64, queue_size=10)

def fg_close():
	t0 = rospy.Time.now().to_sec()
	t1 = t0
	rate2 = rospy.Rate(50)
	while (t1 - t0) < 2:
		pub_fg.publish()
		t1 = rospy.Time.now().to_sec()
		rate2.sleep()

def fg_open():
	t0 = rospy.Time.now().to_sec()
	t1 = t0
	while (t1 - t0) < 2:
		pub_fg.publish(-5)
		t1 = rospy.Time.now().to_sec()
		rate.sleep()

def flaps_open(x):
	t0 = rospy.Time.now().to_sec()
	t1 = t0
	while (t1 - t0) < 2:
		pub_lf.publish(x)
		pub_rf.publish(-x)
		t1 = rospy.Time.now().to_sec()
		rate.sleep()

def flaps_close(x):
	t0 = rospy.Time.now().to_sec()
	t1 = t0
	rate3 = rospy.Rate(200)
	while (t1 - t0) < 3:
		pub_lf.publish(-x)
		pub_rf.publish(x)
		t1 = rospy.Time.now().to_sec()
		rate3.sleep()

def flaps_closed_state():
	t0 = rospy.Time.now().to_sec()
	t1 = t0
	while (t1 - t0) < 2:
		pub_lf.publish(-1)
		pub_rf.publish(1)
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

## RUN ##
speed = Twist()

sub_ls = rospy.Subscriber('/umic_bot/laser/scan', LaserScan, callback)
pub_df = rospy.Publisher('/bot1_diffdrive_controller/cmd_vel', Twist, queue_size=10)

rate = rospy.Rate(10)

fg_close()
flaps_open(1)

while not rospy.is_shutdown():
	color = "Red"
	if color == "Red":
		print(distance)
		flaps_close(1)
		while distance > 0.22:
			speed.linear.x = 0.15
			speed.angular.z = 0
			pub_df.publish(speed)
		
		speed.linear.x = 0
		speed.angular.z = 0
		pub_df.publish(speed)
		
		rotate(0.3, 2)
			
		flaps_open(30)
		flaps_close(1)
		time.sleep(0.5)
		
		rotate(-0.3, 2.5)
	
	elif color == "Green":
		print(distance)
		while distance >= 0.24:
			speed.linear.x = 0.15
			speed.angular.z = 0
			pub_df.publish(speed)
		
		speed.linear.x = 0
		speed.angular.z = 0
		
		fg_open()
		flaps_close(30)
		fg_close()
		flaps_close(1)
		

	pub_df.publish(speed)
	rate.sleep()


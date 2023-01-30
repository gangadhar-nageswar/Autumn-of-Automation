#!/usr/bin/env python


import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
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

sub = rospy.Subscriber('/umic_bot/laser/scan', LaserScan, callback)

rate = rospy.Rate(10)
catpure = True

i=0
while i < 30:
	print(distance)
	rate.sleep()
	i+=1

print(distance,'middle')

distance = 43

while i < 30:
	print('Top')
	print(distance, 'second')
	rate.sleep()

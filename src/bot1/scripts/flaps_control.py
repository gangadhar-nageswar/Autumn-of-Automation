#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import math
import time

rospy.init_node('flaps_control', anonymous=True)

pub_fg = rospy.Publisher('/bot1_frontgate_controller/command', Float64, queue_size=10)
pub_bg = rospy.Publisher('/bot1_backgate_controller/command', Float64, queue_size=10)
pub_lf = rospy.Publisher('/bot1_lf_controller/command', Float64, queue_size=10)
pub_rf = rospy.Publisher('/bot1_rf_controller/command', Float64, queue_size=10)
rate = rospy.Rate(10)

temp = 0
def init():
	 t = rospy.Time.now().to_sec()

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
	while (t1 - t0) < 4:
		pub_fg.publish(-5)
		t1 = rospy.Time.now().to_sec()
		rate.sleep()

def flaps_open():
	t0 = rospy.Time.now().to_sec()
	t1 = t0
	while (t1 - t0) < 2:
		pub_lf.publish(1)
		pub_rf.publish(-1)
		t1 = rospy.Time.now().to_sec()
		rate.sleep()

def flaps_close():
	t0 = rospy.Time.now().to_sec()
	t1 = t0
	while (t1 - t0) < 4:
		pub_lf.publish(-20)
		pub_rf.publish(20)
		t1 = rospy.Time.now().to_sec()
		rate.sleep()

init()
flaps_open()
fg_open()
flaps_close()
fg_close()


#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import math

rospy.init_node('flaps_control', anonymous=True)

pub_lf = rospy.Publisher('/bot1_lf_controller/command', Float64, queue_size=10)
pub_rf = rospy.Publisher('/bot1_rf_controller/command', Float64, queue_size=10)
rate = rospy.Rate(100)

def open_flaps():
	while not rospy.is_shutdown():
		pub_lf.publish(1)
		pub_rf.publish(-1)
		
if __name__ == "__main__":
  try:
  	open_flaps()


  	
  except rospy.ROSInterruptException:
  	pass

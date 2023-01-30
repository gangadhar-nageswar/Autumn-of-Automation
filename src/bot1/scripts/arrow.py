#!/usr/bin/env python
 

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
import numpy as np
from math import atan2,asin
from std_msgs.msg import String
import matplotlib.pyplot as plt
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError
pub = rospy.Publisher('arrow_msg', String, queue_size=1)
bridge = CvBridge()
color_boundaries = [ # colors can be changed
	#([17, 15, 100], [90, 96, 255]), #red
	#([20, 90, 4], [90, 255, 100]), #green
	([0, 90, 90], [20, 120, 120]) # yellow
]

min_area = 5 #toggle-able value
darkness = 60 #toggle-able value



def is_arrow(cnt):
    epsilon = 0.012*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    if(len(approx)<7):
        pass
    else:
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        approx = np.array(approx)
        approx_x = approx[:, 0, 0]      #all x coordinates of the contour points
        mask1 = approx_x > cx
        mask2 = approx_x < cx
        test = len(approx_x[mask1])-len(approx_x[mask2])
        if(test<=2 and test>=-2):
            pass
        elif(test>2):
            turn_right(cnt)
        else:
            turn_left(cnt)

def turn_left(cnt):
    if(cv2.contourArea(cnt)>min_area):
        #rostopic to turn left
        pub.publish('left')
        rospy.loginfo("going left")
    else:
        pass

def turn_right(cnt):
    if(cv2.contourArea(cnt)>min_area):
    #rostopic to turn right
        pub.publish('right')
        rospy.loginfo("going right")
    else:
        pass







def show_image(img):
    cv2.imwrite('/home/aryan/mybot_ws/src/mybot_description/scripts/lol.jpg',img)
    img=cv2.imread('/home/aryan/mybot_ws/src/mybot_description/scripts/lol.jpg')
    plt.imshow(img)
   
    cv2.waitKey(0)

 
def image_callback(img_msg):
    # 
   # rospy.loginfo(img_msg.header)
    
    # Try to convert the ROS Image message to a CV2 Image
    try:
        cv_image = bridge.imgmsg_to_cv2(img_msg, "passthrough")
        #show_image(cv_image)
        cv2.imwrite('/home/aryan/mybot_ws/src/mybot_description/scripts/lol2.jpg',cv_image)
        img=cv2.imread('/home/aryan/mybot_ws/src/mybot_description/scripts/lol2.jpg')
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (400, 350))  
 
        for (lower,upper) in color_boundaries:

            lower=np.array(lower,dtype='uint8')
            upper=np.array(upper,dtype='uint8')
            mask=cv2.inRange(img,lower,upper)
            output=cv2.bitwise_and(img,img,mask=mask)
              
        segment = output
        gray=cv2.cvtColor(segment,cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(gray, darkness, 255, 0)

        _,contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        for cnt in contours:
            is_arrow(cnt)
        cv2.imshow('',segment)
        cv2.waitKey(300)
    except CvBridgeError, e:
        rospy.logerr("CvBridge Error: {0}".format(e))
   
 
def listener():
    
 
    rospy.init_node('arrow_detection', anonymous=False)

    rospy.Subscriber("/mybot/camera1/image_raw", Image, image_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

 
 
if __name__ == '__main__':
    listener()
 
#cv2.namedWindow("Image Window", 1)

 
 # Loop to keep the program from shutting down unless ROS is shut down, or CTRL+C is pressed
#while not rospy.is_shutdown():
    
  #  rospy.spin()

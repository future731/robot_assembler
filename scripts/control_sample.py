#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import math
from std_msgs.msg import Float64MultiArray

from gazebo_msgs.msg import LinkStates
BASE=1

rospy.init_node('send_motion')

cnt1 = 0.0

pub_msg = Float64MultiArray()
pub = rospy.Publisher('fullbody_controller/command', Float64MultiArray, queue_size = 1)

def callback(msg):
    global cnt1
    cnt1 += 1.0
    # pub_msg.layout.dim[0].size = 4
    pub_msg.data = [math.sin(cnt1 * 6.28 / 1000.0), 0, -math.sin(cnt1 * 6.28 / 1000.0), 0]
# send to robot arm
    pub.publish(pub_msg)

    rospy.loginfo("done")
    rospy.loginfo("{} {}".format(rospy.get_caller_id(), msg.pose[BASE]))


if __name__ == '__main__':
    rospy.Subscriber("/gazebo/link_states", LinkStates, callback)
    rospy.spin()

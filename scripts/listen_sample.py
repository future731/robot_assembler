#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from gazebo_msgs.msg import LinkStates

BASE=1

def callback(msg):
    rospy.loginfo("{} {}".format(rospy.get_caller_id(), msg.pose[BASE]))


if __name__ == '__main__':
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/gazebo/link_states", LinkStates, callback)
    rospy.spin()

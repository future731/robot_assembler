#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import actionlib
import numpy as np
import math
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectoryPoint
from geometry_msgs.msg import PoseArray

rospy.init_node('send_motion')
act_client = actionlib.SimpleActionClient('/fullbody_controller/follow_joint_trajectory', FollowJointTrajectoryAction)

act_client.wait_for_server()

def move():
    print("move")
    # gen msg
    traj_msg = FollowJointTrajectoryGoal()
    traj_msg.trajectory.header.stamp = rospy.Time.now() + rospy.Duration(0.2)
    traj_msg.trajectory.joint_names = ['JOINT0', 'JOINT1', 'JOINT2', 'JOINT3', 'JOINT4']
    traj_msg.trajectory.points.append(
            JointTrajectoryPoint(positions=[-1.0, 0, 1.0, 0.0, 0.0], #姿勢1
            time_from_start = rospy.Duration(1))) ## 前の姿勢から1sec
    act_client.send_goal(traj_msg)
    act_client.wait_for_result()
    rospy.signal_shutdown("move")
    rospy.loginfo("done")

def euc_distance(a, b):
    return math.hypot(math.hypot(a.x - b.x, a.y - b.y), a.z - b.z)


moved = False
start_moving = False
history = []
index = 0
def callback(msg):
    global index
    global moved
    global start_moving
    # outlier detection
    if not msg.poses:
        return
    if index == 0 or (index != 0 and euc_distance(msg.poses[0].position, history[index - 1]) < 0.1):
        history.append(msg.poses[0].position)
        print(msg.poses[0].position)
        index = index + 1

    if index > 4 and euc_distance(history[index - 1], history[index - 10]) > 0.1:
        moved = True
        if not start_moving:
            move()
        start_moving = True



if __name__ == '__main__':
    rospy.Subscriber('/ball/HSI_color_filter/cluster_decomposer/centroid_pose_array', PoseArray, callback)
    rospy.spin()

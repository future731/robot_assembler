#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import actionlib
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectoryPoint

rospy.init_node('kick')
act_client = actionlib.SimpleActionClient('/robot2/fullbody_controller/follow_joint_trajectory', FollowJointTrajectoryAction)

act_client.wait_for_server()

# gen msg
traj_msg = FollowJointTrajectoryGoal()
traj_msg.trajectory.header.stamp = rospy.Time.now() + rospy.Duration(0.2)
traj_msg.trajectory.joint_names = ['JOINT0', 'JOINT1', 'JOINT2', 'JOINT3', 'JOINT4']

##
traj_msg.trajectory.points.append(JointTrajectoryPoint(positions=[-2.0, 0, 0, 0, 1.2], #姿勢1
                                                       time_from_start = rospy.Duration(1))) ## 前の姿勢から1sec
traj_msg.trajectory.points.append(JointTrajectoryPoint(positions=[2.0, 0, 0, 0, 1.2], #姿勢2
                                                       time_from_start = rospy.Duration(1.5)))## 前の姿勢から1sec
traj_msg.trajectory.points.append(JointTrajectoryPoint(positions=[0, 0, 0, 0, 0], #姿勢4
                                                       time_from_start = rospy.Duration(4)))## 前の姿勢から2sec

# send to robot arm
act_client.send_goal(traj_msg)

act_client.wait_for_result()

rospy.loginfo("done")

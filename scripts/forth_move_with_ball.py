#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import actionlib
import numpy as np
import math
import tf
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectoryPoint
from geometry_msgs.msg import PoseArray
from geometry_msgs.msg import PoseStamped


rospy.init_node('send_motion')

listener = tf.TransformListener()

act_client = actionlib.SimpleActionClient('/robot1/fullbody_controller/follow_joint_trajectory', FollowJointTrajectoryAction)

act_client.wait_for_server()

def move(pos=[-2.0, 0, 2.0, 0.0, 0.0]):
    print("move")
    # gen msg
    traj_msg = FollowJointTrajectoryGoal()
    traj_msg.trajectory.header.stamp = rospy.Time.now() + rospy.Duration(0.2)
    traj_msg.trajectory.joint_names = ['JOINT0', 'JOINT1', 'JOINT2', 'JOINT3', 'JOINT4']
    traj_msg.trajectory.points.append(
            JointTrajectoryPoint(positions=pos, #姿勢1
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
    global listener
    print("po")
    # outlier detection
    if not msg.poses:
        return
    pose_opt = msg.poses[0]
    t = listener.getLatestCommonTime("/robot1/world", "/robot1/LINKCAMOPT")
    pl = PoseStamped()
    pl.header.frame_id = "robot1/LINKCAMOPT"
    pl.pose = pose_opt
    pose_world = listener.transformPose("/robot1/world", pl)
    if index == 0 or (index != 0 and euc_distance(pose_world.pose.position, history[index - 1]) < 0.3):
        print(pose_world.pose.position)
        history.append(pose_world.pose.position)
        index = index + 1

    if index > 4 and euc_distance(history[index - 1], history[index - 10]) > 0.1:
        moved = True
        if not start_moving:
            if history[index - 1].x > 0:
                move(pos=[-2.0, 0, 2.0, 0.0, 0.0])
            else:
                move(pos=[2.0, 0, -2.0, 0.0, 0.0])
        start_moving = True



if __name__ == '__main__':
    rospy.Subscriber('/ball/HSI_color_filter/cluster_decomposer/centroid_pose_array', PoseArray, callback)
    rospy.spin()

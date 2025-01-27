#!/usr/bin/env python

import rospy
import sys
import tf
from nav_msgs.msg import Odometry

def update_tf(data):
  transform_from = "{}/base_link".format(ns)
  transform_to   = "world"
  pos = data.pose.pose.position
  ori = data.pose.pose.orientation
  orientation = [ori.x, ori.y, ori.z, ori.w]
  position    = [pos.x, pos.y, pos.z]
  br = tf.TransformBroadcaster()
  br.sendTransform(position, orientation, rospy.Time.now(), transform_from, transform_to)
if __name__ == '__main__':
  ns = sys.argv[1]
  rospy.init_node("tf_broadcaster_{}".format(ns.split('_')[1]))
  pose_subscriber = rospy.Subscriber("{}/ground_truth_pose".format(ns), Odometry, update_tf)
  rospy.spin()

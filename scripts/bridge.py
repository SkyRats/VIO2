#!/usr/bin/env python3

import rclpy
from rclpy import qos
from rclpy.node import Node
from rclpy.clock import Clock
from nav_msgs.msg import Odometry
from mavros_msgs.msg import CompanionProcessStatus

class realsense_bridge(Node):

    def __init__(self):
        super().__init__('realsense_bridge')
        self.odometry_sub = self.create_subscription(Odometry, '/camera/odom/sample', self.odometry_callback, qos.qos_profile_sensor_data)
        self.odometry_pub = self.create_publisher(Odometry,  '/mavros/odometry/out', 5)
        self.companion_computer_pub = self.create_publisher(CompanionProcessStatus, '/mavros/companion_process/status', 1)
        self.odom_output = Odometry()
        self.mav_comp_id_msg = CompanionProcessStatus()
    
    def odometry_callback(self, data):
        self.odom_output = data
        self.odom_output.header.frame_id = data.header.frame_id
        self.odom_output.child_frame_id = data.child_frame_id 
        self.odometry_pub.publish(self.odom_output)

        self.mav_comp_id_msg.header.stamp = Clock().now().to_msg() 
        self.mav_comp_id_msg.state = 4 #MAV_STATE_ACTIVE
        self.mav_comp_id_msg.component = 197 # MAV_COMP_ID_VISUAL_INERTIAL_ODOMETRY
        self.companion_computer_pub.publish(self.mav_comp_id_msg)
    
if __name__ == '__main__':
    rclpy.init()
    rs_b = realsense_bridge()
    rclpy.spin(rs_b)

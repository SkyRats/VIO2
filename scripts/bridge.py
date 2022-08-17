#!/usr/bin/env python3

import rclpy
from rclpy import qos
from rclpy.node import Node
from nav_msgs.msg import Odometry
from mavros_msgs.msg import CompanionProcessStatus

class realsense_bridge(Node):

    def __init__(self):
        super().__init__('realsense_bridge')
        self.odometry = Odometry()
        self.odometry_sub = self.create_subscription(Odometry, '/camera/odom/sample', self.odometry_callback, qos.qos_profile_sensor_data)
        self.odometry_pub = self.create_publisher(Odometry,  '/mavros/odometry/out', 5)
        self.mav_comp_id_msg = CompanionProcessStatus()
        self.companion_computer_pub = self.create_publisher(CompanionProcessStatus, '/mavros/companion_process/status', 1)
    
    def odometry_callback(self, data):
        self.odometry_pub.publish(data)

        self.mav_comp_id_msg.header.stamp = Clock().now().to_msg()
        self.mav_comp_id_msg.component = 197 # MAV_COMP_ID_VISUAL_INERTIAL_ODOMETRY

        self.companion_computer_pub.publish(self.mav_comp_id_msg)
    
if __name__ == '__main__':
    rclpy.init()
    rs_b = realsense_bridge()
    rclpy.spin(rs_b)

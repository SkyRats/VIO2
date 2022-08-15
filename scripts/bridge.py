#!/usr/bin/env python3

import rclpy
from rclpy import qos
from rclpy.node import Node
from nav_msgs.msg import Odometry

class realsense_bridge(Node):

    def __init__(self):
        super().__init__('realsense_bridge')
        self.odometry = Odometry()
        self.odometry_sub = self.create_subscription(Odometry, '/camera/pose/sample', self.odometry_callback, qos.qos_profile_sensor_data)
        self.odometry_pub = self.create_publisher(Odometry,  '/mavros/odometry/out', 5)
    
    def odometry_callback(self, data):
        self.odometry_pub.publish(data)
    
if __name__ == '__main__':
    rclpy.init()
    rs_b = realsense_bridge()
    rclpy.spin(rs_b)
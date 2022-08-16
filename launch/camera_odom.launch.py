#!/usr/bin/env python3

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, ExecuteProcess, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    """Launch t265 Intel Realsense camera with the px4 bridge"""
    realsense_launch_dir = os.path.join(get_package_share_directory('realsense2_camera'), 'launch')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([realsense_launch_dir, '/rs_launch.py']),
            launch_arguments={'publish_odom_tf': 'false'}.items(),
        ),
        Node(
            package='realsense_mav_bridge',
            executable='bridge.py',
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='tf_baselink_cameraPose',
            arguments = ["0", "0", "0", "0", "1.5708", "0", "base_link", "camera_pose_frame"],
            output="screen"
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='tf_odom_cameraOdom',
            arguments = ["0", "0", "0", "0", "0", "0", "odom", "camera_odom_frame"],
            output="screen"
        ),
])

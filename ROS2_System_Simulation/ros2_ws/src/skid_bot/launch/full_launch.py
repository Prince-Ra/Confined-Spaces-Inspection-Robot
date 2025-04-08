import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
    package_name = 'skid_bot'

    # Robot State Publisher
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory(package_name), 'launch', 'rsp.launch.py')]
        ),
        launch_arguments={'use_sim_time': 'true'}.items()
    )
    
    # Gazebo simulation environment with custom world
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]
    ),
        launch_arguments={
            'world': os.path.join(get_package_share_directory(package_name), 'worlds', 'maze.world')}.items()
    )   


    # Spawn robot entity into Gazebo
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'skid_bot'],
        output='screen'
    )

    # Static TF for camera
    static_tf_camera = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments=['0', '0', '0', '-1.5708', '0', '-1.5708', 'camera_link', 'camera_optical_link'],
        parameters=[{'use_sim_time': True}],
        output='screen'
    )

    # RViz2
    rviz2 = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )

    # Joystick input
    joy_node = Node(
        package='joy',
        executable='joy_node',
        name='joy_node',
        parameters=[{'use_sim_time': True}],
        output='screen'
    )

    # Teleop twist for joystick
    teleop_node = Node(
        package='teleop_twist_joy',
        executable='teleop_node',
        name='teleop_twist_joy',
        parameters=[{'use_sim_time': True}],
        output='screen'
    )

    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
        static_tf_camera,
        rviz2,
        joy_node,
        teleop_node
    ])

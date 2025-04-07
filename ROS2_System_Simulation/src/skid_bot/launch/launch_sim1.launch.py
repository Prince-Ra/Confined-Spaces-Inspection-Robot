import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node


def generate_launch_description():
    package_name = 'skid_bot'  # <-- your robot's package name

    # Launch robot_state_publisher with simulation time enabled
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(package_name), 'launch', 'rsp.launch.py')
        ]),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Launch Ignition Gazebo (Fortress) with an empty world or your custom world
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('ros_ign_gazebo'), 'launch', 'ign_gazebo.launch.py')
        ]),
        launch_arguments={'ign_args': '-r -v 4 empty.sdf'}.items()  # replace 'empty.sdf' if needed
    )

    # Spawn the robot into Ignition using ros_ign_gazebo/create
    spawn_entity = Node(
        package='ros_ign_gazebo',
        executable='create',
        arguments=[
            '-name', 'skid_bot',
            '-topic', 'robot_description',
        ],
        output='screen'
    )

    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
    ])

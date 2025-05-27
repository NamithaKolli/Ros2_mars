from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mars_week1_cpp_pkg',
            executable='number_publisher',
            name='number_publisher_node',
            output='screen'
        ),
        Node(
            package='mars_week1_cpp_pkg',
            executable='square_subscriber',
            name='square_subscriber_node',
            output='screen'
        )
    ])



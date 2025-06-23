from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    urdf_path = PathJoinSubstitution([
        FindPackageShare('my_robo1_py_pkg'),
        'urdf',
        'my_robo1.urdf.xacro'
    ])

    gazebo_process = ExecuteProcess(
        cmd=['gazebo.gz', 'gazebo'],
        output='screen'
    )

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{
            'robot_description': Command([
                'xacro', urdf_path  # <-- KEY FIX: separate list elements
            ])
        }],
        output='screen'
    )

    spawn_entity = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name', 'my_robot',
            '-topic', 'robot_description'
        ],
        output='screen'
    )

    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/model/my_robot/tf@tf2_msgs/msg/TFMessage[ignition.msgs.Pose_V'
        ],
        output='screen'
    )

    return LaunchDescription([
        gazebo_process,
        robot_state_publisher,
        spawn_entity,
        bridge
    ])


from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    Gesture_Node = Node(
        package='car_project',
        executable='GestureControl.py',
        name='gesture_control',
    )

    Distance_Node = Node(
        package='car_project',
        executable='DistanceSensor.py',
        name='distance_sensor',
    )

    Control_Node = Node(
        package='car_project',
        executable='control.py',
        name='control_node',
    )

    return LaunchDescription([
        Gesture_Node,
        Distance_Node,
        Control_Node
    ])

#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int32
import serial

class ControlNode(Node):
    def __init__(self):
        super().__init__('control_node')
        
        self.serial_port = "/dev/ttyACM0"
        self.baud_rate = 115200
        self.stop_distance = 20

        # Initialize serial communication with Arduino
        self.arduino = serial.Serial(self.serial_port, self.baud_rate, timeout=1)
        self.arduino.flush()

        # Subscribers
        self.gesture_subscription = self.create_subscription(
            String,
            'gesture',
            self.gesture_callback,
            10
        )
        self.distance_subscription = self.create_subscription(
            Int32,
            'distance',
            self.distance_callback,
            10
        )
        
        self.object_close = False
        self.last_command = ""  
   
    def gesture_callback(self, msg):
        if not self.object_close:
            command = msg.data
            if command != self.last_command:
                self.arduino.write(command.encode('utf-8'))
                self.get_logger().info(f'Sent gesture command: {command}')
                self.last_command = command  # Update last command


    def distance_callback(self, msg):
        distance = msg.data
        if distance < self.stop_distance:
            self.object_close = True
            self.send_command_to_arduino('6\n')
            self.get_logger().info('Obstacle too close. Stopping the car.')
        else:
            self.object_close = False

def main(args=None):
    rclpy.init(args=args)
    node = ControlNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

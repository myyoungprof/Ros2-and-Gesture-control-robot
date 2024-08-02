#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import serial
import re

class DistanceSensor(Node):
    def __init__(self):
        super().__init__('distance_sensor')
        self.serial_port = "/dev/ttyACM0"
        self.baud_rate = 115200

        self.publisher_ = self.create_publisher(Int32, 'distance', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)

        self.arduino = serial.Serial(self.serial_port, self.baud_rate, timeout=1)
        self.arduino.flush()

    def timer_callback(self):
        if self.arduino.in_waiting > 0:
            line = self.arduino.readline().decode('utf-8').rstrip()
            match = re.search(r'Distance: (\d+) cm', line)
            if match:
                distance = int(match.group(1))
                msg = Int32()
                msg.data = distance
                self.publisher_.publish(msg)
                self.get_logger().info(f'Distance: {distance}')

def main(args=None):
    rclpy.init(args=args)
    node = DistanceSensor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

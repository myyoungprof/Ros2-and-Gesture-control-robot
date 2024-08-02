# #!/usr/bin/env python3

# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import String, Int32
# import serial

# class CarControlNode(Node):
#     def __init__(self):
#         super().__init__('car_control')
#         self.subscription_gesture = self.create_subscription(
#             String,
#             'gesture_command',
#             self.gesture_callback,
#             10
#         )
#         self.subscription_distance = self.create_subscription(
#             Int32,
#             'distance',
#             self.distance_callback,
#             10
#         )
#         self.arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
#         self.arduino.flush()

#         self.object_close = False
#         self.last_sent_command = None

#     def send_command_to_arduino(self, command):
#         if command != self.last_sent_command:
#             self.arduino.write(command.encode('utf-8'))
#             self.last_sent_command = command

#     def gesture_callback(self, msg):
#         if not self.object_close:
#             self.send_command_to_arduino(f'{msg.data}\n')

#     def distance_callback(self, msg):
#         distance = msg.data
#         if distance < 20:
#             self.object_close = True
#             self.send_command_to_arduino('stop\n')
#         else:
#             self.object_close = False

# def main(args=None):
#     rclpy.init(args=args)
#     node = CarControlNode()
#     rclpy.spin(node)
#     node.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()

#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_interfaces.msg import HardwareStatus

class HardwareStatusPublisherNode(Node):
    def __init__(self):
        super().__init__("hw_status_publisher")
        self._publisher = self.create_publisher(HardwareStatus, "hardware_status", 10)
        self._timer=self.create_timer(0.5, self.publish_message)
        self.get_logger().info("Hardware Status Node has been started")
    
    def publish_message(self):
        msg = HardwareStatus()
        msg.temperature = 45
        msg.are_motors_ready = True
        msg.debug_info = "Tudo ok com os motores"
        self._publisher.publish(msg)

def main (args=None):
    rclpy.init(args=args)
    node = HardwareStatusPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()
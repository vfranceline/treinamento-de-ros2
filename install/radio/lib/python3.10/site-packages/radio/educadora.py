#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from example_interfaces.msg import String

class EducadoraNode(Node):
    def __init__(self):
        super().__init__("educadora")
        self._publisher1 = self.create_publisher(String, "FM1075", 10)
        self._publisher2 = self.create_publisher(String, "AM536", 10)

        self._timer = self.create_timer(0.5, self.publish_message)
        self.get_logger().info("A rádio educadora entrou no ar")

    def publish_message(self):
        msg_fm = String()
        msg_fm.data = 'Transmitindo em FM: Olá Bahia'
        self._publisher1.publish(msg_fm)

        msg_am = String()
        msg_am.data = 'Transmitindo em AM: Olá Bahia'
        self._publisher2.publish(msg_am)


def main(args=None):
    rclpy.init(args=args)
    node = EducadoraNode()
    rclpy.spin(node)
    rclpy.shutdown()
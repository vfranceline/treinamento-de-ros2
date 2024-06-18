#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class PredatorControllerNode(Node):
    def __init__(self):
        super().__init__("predator_controller")

    def main(args=None):
        rclpy.init(args=args)
        node = PredatorControllerNode()
        rclpy.spin(node)
        rclpy.shutdown()
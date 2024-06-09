#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts

class CalculatorServerNode(Node):
    def __init__(self):
        super().__init__("calculator_server")
        self._server = self.create_service(AddTwoInts, "add_two_ints", self.callback_add_two_ints)

        self.get_logger().info("calculadora on")
    
    def callback_add_two_ints(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(str(request.a) + " + " + str(request.b) + " = " + str(response.sum))
        return response

    
def main(args=None):
    rclpy.init(args=args)
    node = CalculatorServerNode()
    rclpy.spin(node)
    rclpy.shutdown()
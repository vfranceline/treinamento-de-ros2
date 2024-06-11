#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_interfaces.srv import Calc

class CalculadoraBasicaServerNode(Node):
    def __init__(self):
        super().__init__("calculadora_basica_server")
        self._server = self.create_service(Calc,"display", self.callback_operacao)

        self.get_logger().info("calculadora on")

    def callback_operacao(self, request, response):
        if request.op == '+':
            response.result = request.a + request.b
        elif request.op == '-':
            response.result = request.a - request.b
        elif request.op == '*':
            response.result = request.a * request.b
        else:
            response.result = request.a / request.b
        
        self.get_logger().info(str(request.a) + str(request.op) + str(request.b) + " = " + str(response.result))
        return response

def main(args=None):
    rclpy.init(args=args)
    node = CalculadoraBasicaServerNode()
    rclpy.spin(node)
    rclpy.shutdown()

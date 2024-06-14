#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from my_interfaces.srv import Calc

class CalculadoraBasicaServerNode(Node):
    def __init__(self):
        super().__init__("calculadora_basica_server")
        self._server = self.create_service(Calc,"calculadora_basica", self.callback_operacao)
        self._pub = self.create_publisher(String, "Display", 10)
        self._timer = None
        self._displaymsg = String()

        self.get_logger().info("calculadora on")

    def callback_operacao(self, request, response):
        response.status = "Operação realizada!"
        try:
            match request.op:
                case "+":
                    response.resultado = request.a + request.b
                case "-":
                    response.resultado = request.a - request.b
                case "*":
                    response.resultado = request.a * request.b
                case "/":
                    response.resultado = request.a / request.b
                case _:
                    response.status = "Operação não realizada!"
        except Exception as e:
            response.status = "Operação não realizada!"

        if response.status == "Operação realizada!":
            self._displaymsg.data = f'{request.a} {request.op} {request.b} = {response.resultado}'
        else:
            self._displaymsg.data = 'Operação não realizada!'

        self._timer = self.create_timer(0.5, self.publish_message)
        return response
    
    def publish_message(self):
        self._pub.publish(self._displaymsg)
        self.get_logger().info(self._displaymsg.data)

def main(args=None):
    rclpy.init(args=args)
    node = CalculadoraBasicaServerNode()
    rclpy.spin(node)
    rclpy.shutdown()

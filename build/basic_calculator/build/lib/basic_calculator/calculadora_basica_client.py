#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_interfaces.srv import Calc

from functools import partial

class CalculadoraBasicaClientNode(Node):
    def __init__(self):
        super().__init__("client")
        self.get_logger().info("O cliente da calculadora está rodando")
        self.call_calculator_server(3.0, 4.0, '+')

    def call_calculator_server(self, a, b, op):
        client = self.create_client(Calc, "calculadora_basica")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Estou aguardando o serviço calc ser iniciado")
        self.get_logger().info("Opa! Ligaram a calculadora")

        request = Calc.Request()
        request.a = a
        request.b = b
        request.op = op

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_call_calc, request=request))
    
    def callback_call_calc(self, future, request):
        try:
            response=future.result()
            self.get_logger().info(str(request.a) + str(request.op) + str(request.b) + "=" + str(response.result))
        except Exception as e:
            self.get_logger().error("Chamada de serviço falhou")

def main(args=None):
    rclpy.init(args=args)
    node = CalculadoraBasicaClientNode()
    rclpy.spin(node)
    rclpy.shutdown()
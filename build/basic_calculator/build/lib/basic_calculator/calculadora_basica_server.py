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
                case 'soma':
                    response.result = request.a + request.b
                case 'subtração':
                    response.result = request.a - request.b
                case 'multiplicação':
                    response.result = request.a * request.b
                case 'divisão':
                    response.result = request.a / request.b
                case _:
                    response_status = "Operação não realizada!"
        except Exception as e:
            response.status = "Operação não realizada :("

        if response.status == "Operação realizada!":
            self._displaymsg.data = f'{request.a} {request.op} {request.b} = {response.result}'
        else:
            self._displaymsg.data = 'Operação não realizada!'

        self._timer = self.create_timer(0.5, self.publish_message)
        return response
    
    def publish_message(self):
        self._pub.publish(self._displaymsg)
        self.get_logger().info(self._displaymsg.data)

        # if request.op == 'soma':
        #     response.result = request.a + request.b
        #     self.get_logger().info(str(request.a) + "+" + str(request.b) + " = " + str(response.result))
        #     return response
            
        # if request.op == 'subtração':
        #     response.result = request.a - request.b
        #     self.get_logger().info(str(request.a) + "-" + str(request.b) + " = " + str(response.result))
        #     return response
        
        # if request.op == 'multiplicação':
        #     response.result = request.a * request.b
        #     self.get_logger().info(str(request.a) + "*" + str(request.b) + " = " + str(response.result))
        #     return response
        
        # if request.op == 'divisão':
        #     response.result = request.a / request.b
        #     self.get_logger().info(str(request.a) + "/" + str(request.b) + " = " + str(response.result))
        #     return response

def main(args=None):
    rclpy.init(args=args)
    node = CalculadoraBasicaServerNode()
    rclpy.spin(node)
    rclpy.shutdown()

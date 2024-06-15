from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    remap_calculator_service = ("add_two_ints", "soma2ints")
    calculator_server_node = Node(
        package="calculator",
        executable="calculator_server",
        name="Calculadora_Servidor",
        remappings=[
            remap_calculator_service            
        ]
    )

    calculator_client_node = Node(
        package="calculator",
        executable="calculator_client",
        name="Calculadora_Cliente",
        remappings=[
            remap_calculator_service            
        ]
    )

    calculator_client_param_node = Node(
        package="calculator",
        executable="calculator_client_param",
        name="Calculadora_Cliente_Parametros",
        remappings=[
            remap_calculator_service            
        ],
        parameters=[
            {"argument1":7},
            {"argument2":5}
        ]
    )

    ld.add_action(calculator_server_node)
    ld.add_action(calculator_client_node)
    ld.add_action(calculator_client_param_node)
    return ld
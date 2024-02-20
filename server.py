from concurrent import futures
import logging
import uuid

import grpc
from grpc_reflection.v1alpha import reflection

from pb2 import (
    calculator_pb2,
    calculator_pb2_grpc
)

ID = str(uuid.uuid4())[:8]


class Calculator(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        a = request.a
        b = request.b
        print(f"Inputs: {a}, {b}")
        output = a + b
        return calculator_pb2.CalcOutput(result=output, instance=ID)

    def Subtract(self, request, context):
        a = request.a
        b = request.b
        print(f"Inputs: {a}, {b}")
        output = a - b
        return calculator_pb2.CalcOutput(result=output, instance=ID)

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    SERVICE_NAMES = (
        calculator_pb2.DESCRIPTOR.services_by_name["Calculator"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()

from __future__ import print_function

import logging

import grpc
from pb2 import (
    calculator_pb2,
    calculator_pb2_grpc
)

def run():
    print("Will try to get result ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Add(calculator_pb2.CalcInput(a=5,b=10))
    print(f"Result received: {response.out}")


if __name__ == "__main__":
    logging.basicConfig()
    run()

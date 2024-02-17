service = calculator

generate:
	mkdir -p pb2
	touch pb2/__init__.py
	python -Wignore -m grpc_tools.protoc -I./protos --python_out=./pb2 --pyi_out=./pb2 --grpc_python_out=./pb2 ./protos/$(service).proto
	sed -i 's/$(service)_pb2/pb2.$(service)_pb2/' pb2/$(service)_pb2_grpc.py

build:
	docker build . -t calculator:latest

run:
	docker run --rm -it --name calculator -p 50051:50051 calculator:latest

clean:
	rm -rf pb2/*

proto = calculator

generate:
	mkdir -p pb2
	python -Wignore -m grpc_tools.protoc -I./protos --python_out=./pb2 --pyi_out=./pb2 --grpc_python_out=./pb2 ./protos/$(proto).proto
	sed -i 's/$(proto)_pb2/pb2.$(proto)_pb2/' pb2/$(proto)_pb2_grpc.py

clean:
	rm -rf pb2/*

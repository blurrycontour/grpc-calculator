service = calculator
image = grpc-calculator

generate:
	mkdir -p pb2
	touch pb2/__init__.py
	python -Wignore -m grpc_tools.protoc -I./protos --python_out=./pb2 --pyi_out=./pb2 --grpc_python_out=./pb2 ./protos/$(service).proto
	sed -i 's/$(service)_pb2/pb2.$(service)_pb2/' pb2/$(service)_pb2_grpc.py

build:
	docker build . -t $(image):latest

run:
	docker run --rm -it --name $(image) -p 50051:50051 $(image):latest

push:
	docker tag $(image):latest blurrycontour/$(image):latest
	docker push blurrycontour/$(image):latest
	docker rmi blurrycontour/$(image):latest

clean:
	rm -rf pb2/*

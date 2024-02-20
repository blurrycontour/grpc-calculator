# grpc-calculator

A basic grpc based calculator

## Example in Postman
![image](docs/images/postman.png)

## Run on Google Cloud Run
```bash
gcloud run deploy --image docker.io/blurrycontour/grpc-calculator:latest --platform managed --port 50051
```

## Build
```bash
# Use these commands for easy life
make clean
make
# Docker commands
make build
make run
make push
```

## Load Testing
Locally
```bash
docker run --rm -it --entrypoint sh fullstorydev/grpcurl:latest-alpine -c "while true; do grpcurl -plaintext -d '{\"a\":1, \"b\":2}' localhost:50051 calculator.Calculator/Add; sleep 0; done"
```

##

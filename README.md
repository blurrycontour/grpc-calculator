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

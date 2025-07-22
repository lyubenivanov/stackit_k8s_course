# Exercise 02: Build Docker Image and Push to DockerHub

## Build the Docker image:
```bash
docker build -t <your-dockerhub-username>/item-app:latest .
```

## Push the Docker image to DockerHub:

```bash
docker login
docker push <your-dockerhub-username>/item-app:latest
```
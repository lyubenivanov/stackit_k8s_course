
# Exercise 03: Add a Deployment

## Add a Deployment

Create a new file called `hello-python-deployment.yaml` with the following content:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-python
spec:
  selector:
    matchLabels:
      app: hello-python
  replicas: 2
  template:
    metadata:
      labels:
        app: hello-python
    spec:
      containers:
        - name: hello-python
          image: jasonhaley/hello-python:latest
          ports:
            - containerPort: 80
```
## Apply the Deployment

```bash
kubectl apply -f hello-python-deployment.yaml
```
## Verify the Deployment

```bash
kubectl get deployments
```
## Verify the Pods

```bash
kubectl get pods
```

## Create a Service

Create a new file called `hello-python-service.yaml` with the following content:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: hello-python-service
spec:
  selector:
    app: hello-python
  ports:
    - protocol: TCP
      port: 80
      targetPort: 5000
  type: LoadBalancer
```

## Create the Service

```bash
kubectl apply -f hello-python-service.yaml
```

## Verify the Service

```bash
kubectl get services
```
## Get the External IP

```bash
kubectl get service hello-world-service
```
## Access the Application
Open your web browser and navigate to the external IP address of the service. 
You should see a message from the Python application.

## Add dns record

```bash
stackit dns record-set create --zone-id <ZONE_ID> --name <UNIQUE_NAME> --type A --record <EXTERNAL_IP>
```



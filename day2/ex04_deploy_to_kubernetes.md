# Exercise 04: Deploy to Kubernetes

## Create a ConfigMap for PostgreSQL credentials:

Create a file named `postgres-config.yaml` with the following content:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: postgres-config
data:
  POSTGRES_USER: postgres
  POSTGRES_PASSWORD: postgres
  POSTGRES_DB: demo_db
```

## Apply the ConfigMap:
```bash
kubectl apply -f postgres-config.yaml
```

## Create a Kubernetes Deployment for the item-app: 

Create a file named `item-app-deployment.yaml` with the following content:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: item-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: item-app
  template:
    metadata:
      labels:
        app: item-app
    spec:
      containers:
      - name: item-app
        image: <your-dockerhub-username>/item-app:latest
        ports:
        - containerPort: 5000
        env:
        - name: DATABASE_URL
          value: postgresql://$(POSTGRES_USER):$(POSTGRES_PASSWORD)@db:5432/$(POSTGRES_DB)
        envFrom:
        - configMapRef:
            name: postgres-config
```

## Apply the Deployment:
```bash
kubectl apply -f item-app-deployment.yaml
```
## Create a Kubernetes Service for the item-app:
Create a file named `item-app-service.yaml` with the following content:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: item-app-service
spec:
  selector:
    app: item-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 5000
  type: LoadBalancer
```

## Apply the Service:
```bash
kubectl apply -f item-app-service.yaml
```

## Verify the Deployment and Service:
```bash
kubectl get deployments
kubectl get services
```


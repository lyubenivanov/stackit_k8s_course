
# Exercise 04: Add a Second Deployment with Hello World

## Add a Second Deployment

Create a new file called `hello-world-deployment.yaml` with the following content:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-world
spec:
  selector:
    matchLabels:
      app: hello-world
  replicas: 2
  template:
    metadata:
      labels:
        app: hello-world
    spec:
      containers:
        - name: hello-world
          image: dockerbogo/docker-nginx-hello-world
          ports:
            - containerPort: 80
```

## Apply the Deployment

```bash
kubectl apply -f hello-world-deployment.yaml
```

## Verify the Deployment

```bash
kubectl get deployments
```

## Create a Service for the Second Deployment

```yaml
apiVersion: v1
kind: Service
metadata:
  name: hello-world-service
spec:
  selector:
    app: hello-world
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: ClusterIP
```

## Apply the Service

```bash
kubectl apply -f hello-world-service.yaml
```

## Verify the Service

```bash
kubectl get services
```

## Install Ingress Controller
Use the official YAML manifest to deploy the controller:
```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml
```

## Verify the Ingress Controller

```bash
kubectl get pods -n ingress-nginx
```

## Verify the Ingress External IP

```bash
kubectl get service ingress-nginx-controller -n ingress-nginx
```

## Configure Ingress to Route Traffic
Create a new file called hello-world-ingress.yaml with the following content:
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: hello-world-ingress
spec:
  ingressClassName: nginx
  rules:
    - host: <mysubdomain>.sgsbg-playground.runs.onstackit.cloud
      http:
        paths:
          - path: /world
            pathType: Prefix
            backend:
              service:
                name: hello-world-service
                port:
                  number: 80
```

## Apply the Ingress

```bash
kubectl apply -f hello-world-ingress.yaml
```

## Verify the Ingress

```bash
kubectl get ingress
```

The address should be the external IP of the Ingress controller.

## Add DNS Record

```bash
stackit dns record-set create --zone-id 6e978c62-0b49-4087-b9cc-8bd0e7c9507a --name <your_subdomain> --type A --record <the_external_ip> --ttl 60
```

## Verify the DNS Record

```bash
dig <your_subdomain>.sgsbg-playground.runs.onstackit.cloud
```

For Windows users, you can use the following command to verify the DNS record:
```powershell
Resolve-DnsName <your_subdomain>.sgsbg-playground.runs.onstackit.cloud
```

## Change the Ingress
To change the Ingress to route traffic to the second deployment, update the `hello-world-ingress.yaml` file with the new path and service name:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: hello-world-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
    - host: <mysubdomain>.sgsbg-playground.runs.onstackit.cloud
      http:
        paths:
          - path: /world
            pathType: Prefix
            backend:
              service:
                name: hello-world-service
                port:
                  number: 80
          - path: /python
            pathType: Prefix
            backend:
              service:
                name: hello-python-service
                port:
                  number: 80
```

See

annotations:
nginx.ingress.kubernetes.io/rewrite-target: /

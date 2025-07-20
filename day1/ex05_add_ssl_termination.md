
# Exercise 05: Add SSL Termination to the Nginx Deployment

## Install Cert-Manager

```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.18.2/cert-manager.yaml
```

## Verify the Cert-Manager installation:

```bash
kubectl get pods -n cert-manager
```

## Install helm

Check from the official Helm documentation how to install Helm on your system: https://helm.sh/docs/intro/install/

## Stackit webhook for cert-manager

Check the official Stackit documentation for cert-manager webhook installation: https://github.com/stackitcloud/stackit-cert-manager-webhook

```bash
helm repo add stackit-cert-manager-webhook https://stackitcloud.github.io/stackit-cert-manager-webhook
helm install stackit-cert-manager-webhook --namespace cert-manager stackit-cert-manager-webhook/stackit-cert-manager-webhook
```

```bash
kubectl create secret generic stackit-sa-authentication \
-n cert-manager \
--from-literal=sa.json='{
"id": "4e1fe486-b463-4bcd-9210-288854268e34",
"publicKey": "-----BEGIN PUBLIC KEY-----\nPUBLIC_KEY\n-----END PUBLIC KEY-----",
"createdAt": "2024-04-02T13:12:17.678+00:00",
"validUntil": "2024-04-15T22:00:00.000+00:00",
"keyType": "USER_MANAGED",
"keyOrigin": "GENERATED",
"keyAlgorithm": "RSA_2048",
"active": true,
"credentials": {
"kid": "kid",
"iss": "iss",
"sub": "sub",
"aud": "aud",
"privateKey": "-----BEGIN PRIVATE KEY-----\nPRIVATE-KEY==\n-----END PRIVATE KEY-----"
}
}'
```

Adjust the deployment via helm to use the secret:
```bash
helm upgrade stackit-cert-manager-webhook \
--namespace cert-manager \
stackit-cert-manager-webhook/stackit-cert-manager-webhook \
--set stackitSaAuthentication.enabled=true
```

## Create a ClusterIssuer for Let's Encrypt

Create a file named `letsencrypt-clusterissuer.yaml` with the following content:
```yaml 
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: your-email@example.com
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
      - dns01:
          webhook:
            solverName: stackit
            groupName: acme.stackit.de
            config:
              projectId: 1d3c3bf7-6c5a-4077-804f-3a226cb3903b
```

## Apply the ClusterIssuer

```bash
kubectl apply -f letsencrypt-clusterissuer.yaml
```

## Update the Ingress for SSL Termination

Modify the hello-world-ingress.yaml file to include TLS configuration:
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: hello-world-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  ingressClassName: nginx
  tls:
    - hosts:
        - <your-subdomain>.sgsbg-playground.runs.onstackit.cloud
      secretName: hello-world-tls
  rules:
    - host: <your-subdomain>.sgsbg-playground.runs.onstackit.cloud
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

## Verify SSL Termination
Check the status of the certificate:
```bash
kubectl describe certificate hello-world-tls
```
## Test the SSL Termination

Open your browser and navigate to `https://<your-subdomain>.sgsbg-playground.runs.onstackit.cloud/world` and `https://<your-subdomain>.sgsbg-playground.runs.onstackit.cloud/python`. You should see the respective responses from the hello-world and hello-python services over HTTPS.
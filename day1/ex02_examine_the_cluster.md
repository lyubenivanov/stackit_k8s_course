
# Exercise 02: Examine the Cluster

## View the current kubeconfig
```bash
kubectl config view
```

## Add a custom kubeconfig file
For Windows users, use the following command to add a custom kubeconfig file:
```powershell
$env:KUBECONFIG = "$env:KUBECONFIG;C:\path\to\custom-kubeconfig.yaml"
```
For macOS users, use the following command:
```bash
$env:KUBECONFIG = "$env:KUBECONFIG;C:\path\to\custom-kubeconfig.yaml"
```

## View the current context
```bash
kubectl config current-context
```
## List all contexts
```bash
kubectl config get-contexts
```

## Set the current context
```bash
kubectl config use-context <CLUSTER_NAME>
```

## List all pods

```bash
kubectl get pods --all-namespaces
```

## List all pods in current namespace
```bash
kubectl get pods
```

## List all namespaces
```bash
kubectl get namespaces
```

## Switch the namespace
```bash
kubectl config set-context --current --namespace=<NAMESPACE>
```

## View the current namespace
```bash
kubectl config view --minify | grep namespace:
```

## View the current cluster
```bash
kubectl config view --minify | grep cluster:
```

## Delete the cluster
```bash
stackit ske cluster delete <CLUSTER_NAME> --async
```
## Delete the kubeconfig file
```bash
rm -f ./kubeconfig
```

for Windows users, use the following command to set the KUBECONFIG environment variable:
```powershell
$env:KUBECONFIG = "./kubeconfig"
```
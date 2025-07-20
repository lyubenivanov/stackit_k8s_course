
# Exercise 01: Create a Kubernetes Cluster in Stackit

## Copy the service account key to your local machine
```bash
scp <path_to_sa.json> rocky@<external_ip>:/tmp/sa.json
```

## Setup service account

```bash
stackit auth activate-service-account --service-account-key-path /tmp/sa.json
```

## Generate payload for cluster initial parameters

```bash
stackit ske cluster generate-payload > ./payload.json
```

## Create the Kubernetes cluster

For the cluster name, replace `<CLUSTER_NAME>` with your train_<YOUR_INITIALS>. E.g., `train_jd`.
```bash
stackit ske cluster create <CLUSTER_NAME> --payload @./payload.json --async
```
## Wait for the cluster to be ready

## Download the kubeconfig file
```bash
stackit ske kubeconfig create <CLUSTER_NAME> --filepath ./kubeconfig --expiration 30d
```

## (Optional) Downlad the kubeconfig file to your local machine
```bash
scp rocky@<external_ip>:<path_to_kubeconfig> <local_path_to_kubeconfig>
```

We can now use the kubeconfig file to connect to the cluster.
```bash
export KUBECONFIG=./kubeconfig
```

For Windows users, use the following command to set the KUBECONFIG environment variable:
```powershell
$env:KUBECONFIG = "./kubeconfig"
```

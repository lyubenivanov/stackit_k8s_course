
# Exercise 01: Create a Kubernetes Cluster in Stackit

## Copy the service account key to your local machine

1. Select the project under which you want to create a service account.
2. Navigate to Access > Service accounts.
3. Click Create service account.
4. Enter a prefix for the service account identifier and click Create. 
5. Navigate to IAM and Management > Access
6. Click on the Grant Access button
7. Enter the e-mail address of the service account in the Add subject field
8. Add the Owner role in the Assign roles field
9. Under Access > Service accounts select the service account you want to create a key for
10. Navigate to Service Account Keys
11. Click Create service account key
12. Choose create new key pair: A new key pair will be created and the public key will be stored.
13. Enter a Expiring date (optional)
14. Click Create - Save the generated file to a /tmp/sa.json


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

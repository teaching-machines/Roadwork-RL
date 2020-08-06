# Azure Setup

This guide explains how to install the AZ CLI and utilize it to configure `kubectl`

## Installing AZ CLI

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl apt-transport-https lsb-release gnupg

curl -sL https://packages.microsoft.com/keys/microsoft.asc |
    gpg --dearmor |
    sudo tee /etc/apt/trusted.gpg.d/microsoft.gpg > /dev/null
	
AZ_REPO=$(lsb_release -cs)
echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $AZ_REPO main" |
    sudo tee /etc/apt/sources.list.d/azure-cli.list
	
sudo apt-get update
sudo apt-get install azure-cli

az login
```

## Installing Kubectl

```bash
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
```

## Configuring Kubectl with AZ CLI

```bash
az account set --subscription "SUBSCRIPTION-NAME"
az aks get-credentials --name aks-cluster --resource-group aks-resource-group
```
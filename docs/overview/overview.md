# Overview

Crossplane Assistant is your companion for Crossplane development.

![Crossplane Assistant](./assets/logo.png){: style="width: 100%; max-width: 60%; margin: 0 20%;"}

## Getting Started

Install Crossplane Assistant inside your Kubernetes cluster.

```bash
cd charts/
helm upgrade -i crossplane-assistant -f values.yaml -n crossplane-assistant --create-namespace .
kubectl port-forward -n crossplane-assistant svc/crossplane-assistant 8080:80
```

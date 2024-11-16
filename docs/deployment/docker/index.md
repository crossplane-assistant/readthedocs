# Setup

## Prerequisites

- Kubernetes Cluster
- Kubectl
- Helm

## Installation

```bash
cd charts/
helm upgrade -i crossplane-assistant -f values.yaml -n crossplane-assistant --create-namespace .
```

## Access

### Port Forward

```bash
kubectl port-forward -n crossplane-assistant svc/crossplane-assistant 8080:80
```

### Ingress

Change the following values in the `values.yaml` file:

```yaml
ui:
    ingress:
    enabled: true
    hosts:
        - host: crossplane-assistant.local
        paths:
            - /
```

Then install or update the chart:

```bash
helm upgrade -i crossplane-assistant -f values.yaml -n crossplane-assistant --create-namespace .
```

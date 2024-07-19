# README

## Create Pod
```bash
kubectl.exe -n devopstraining apply -f square-pod.yaml
```
## Expose Application
```bash
kubectl.exe -n devopstraining expose pod square --type=LoadBalancer --name=square-service
```
- You should be able to now access the API at http://localhost:8800/docs
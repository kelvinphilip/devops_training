# README

## Create Deployment
```bash
kubectl.exe -n devopstraining apply -f devops-app-deployment.yml
```

## Check Deployment
```bash
kubectl.exe -n devopstraining get deployment
```

## Expose Application
```bash
kubectl.exe -n devopstraining expose deployment devopstraining-app --type=LoadBalancer --name=devopstraining-service
```

## Accessing the Application
- You should be able to now access the API at http://localhost:8800/docs


## Check Logs
```bash
kubectl.exe -n devopstraining logs -f -lapp=devopstraining-app --all-containers --prefix --timestamps --since=30m


# README

## Create Deployment
```bash
kubectl.exe -n devopstraining apply -f devops-app-deployment.yml
```

## Check Deployment
```bash
kubectl.exe -n devopstraining get deployment
```

## Create Service
```bash
kubectl.exe -n devopstraining apply -f devops-app-service.yml
```

## Check Service
```bash
kubectl.exe -n devopstraining get services
```

## Expose Application
```bash
kubectl.exe -n devopstraining expose service devopstraining-app-service --type=LoadBalancer --name=square-service
```

## Accessing the Application
- You should be able to now access the API at http://localhost:8800/docs


## Check Logs
```bash
kubectl.exe -n devopstraining logs -f -lapp=devopstraining-app --all-containers --prefix --timestamps --since=30m


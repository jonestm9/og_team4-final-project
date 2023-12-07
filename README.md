# og_team4-final-project

In order to start up kubernetes cluster:

```
cd k8s_startup_scripts
./start_k8s.sh
```

helm installation is needed with the following 3 commands before starting the nginx ingress controller: 
```
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
```

to start the ingress controller at a base level, follow the instructions at the following link:
https://kubernetes.github.io/ingress-nginx/deploy/


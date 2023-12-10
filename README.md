# og_team4-final-project

In order to start up kubernetes cluster:

```
cd k8s_startup_scripts
./start_k8s.sh
```
or, if previously started,
```
cd k8s_startup_scripts
./restart_k8s.sh
```

helm installation is needed with the following 3 commands before starting the nginx ingress controller (only needs to be run once): 
```
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
```
to create ingress controller:
```
./start_ingress.sh
```
to test ingress controller:
```
curl http://demo1.localdev.me:8080/
curl http://demo2.localdev.me:8080/
```

## Trevor's next steps
- looking into SSL termination utilizing this ingress resource
- eventually, connecting to OAuth


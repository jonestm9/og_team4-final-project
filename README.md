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

## Trevor's next steps

- after booting ingress controller to namespace and deploying our services in pods
- create ingress resource (https://kubernetes.io/docs/concepts/services-networking/ingress/) and setting up paths to our microservices
- find out if it is still not a "real" kubernetes cluster once all is deployed - if not, troubleshoot, since this prevents load balancer from kicking in
- looking into SSL termination utilizing this ingress resource
- eventually, connecting to OAuth (dependent on external-facing ip, from 2 bullets above)


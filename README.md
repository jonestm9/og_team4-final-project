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

to create the ingress controller using helm:
```
helm upgrade --install ingress-nginx ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace ingress-nginx --create-namespace
```
this creates this ingress controller from the provided repository, under the namespace ingress-nginx.
using the following 2 commands:
```
kubectl create deployment demo --image=httpd --port=80
kubectl expose deployment demo
```
the create deployment works similar to kubectl apply with our yaml files we used earlier in the year.
this creates a deployment named "demo" on port 80, with the image as httpd (which is a demo web server image).

For our purposes, I think we would need to run these commands multiple times with our given docker image link and the port we want to run our microservices on.


kubectl expose deployment demo makes it visible outside of the k8 cluster, so that outside traffic can access it.

this is supposed to create an Ingress resource, this one specifically uses a host that maps to localhost:
```
kubectl create ingress demo-localhost --class=nginx \
  --rule="demo.localdev.me/*=demo:80"
```

the following command forwards a local port to the ingress controller
```
kubectl port-forward --namespace=ingress-nginx service/ingress-nginx-controller 8080:80
```

and we can see them communicating using this command:
```
curl --resolve demo.localdev.me:8080:127.0.0.1 http://demo.localdev.me:8080
```
now, the goal is to figure out how to extrapolate this example code to have multiple different things running on different ports and still accessible through the ingress controller and port-forwarding.

https://kubernetes.github.io/ingress-nginx/deploy/

## Trevor's next steps

- after booting ingress controller to namespace and deploying our services in pods
- create ingress resource (https://kubernetes.io/docs/concepts/services-networking/ingress/) and setting up paths to our microservices
- find out if it is still not a "real" kubernetes cluster once all is deployed - if not, troubleshoot, since this prevents load balancer from kicking in
- looking into SSL termination utilizing this ingress resource
- eventually, connecting to OAuth (dependent on external-facing ip, from 2 bullets above)


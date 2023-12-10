# og_team4-final-project

In order to start up kubernetes cluster:

```
cd k8s_startup_scripts
./start_k8s.sh
```

helm installation is needed with the following 3 commands before starting the nginx ingress controller (only needed to be run once): 
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
using the following 4 commands:
```
kubectl create deployment demo-service1 --image=httpd --port=8081

kubectl expose deployment demo-service1 --port=80

kubectl create deployment demo-service2 --image=nginx --port=8082

kubectl expose deployment demo-service2 --port=80
```
the create deployment works similar to kubectl apply with our yaml files we used earlier in the year.
this creates a deployment named "demo" on port 80, with one image as httpd and one as nginx, both just web server images.

kubectl expose deployment demo makes it visible outside of the k8 cluster, so that outside traffic can access it.

this creates an Ingress resource, this one specifically uses a host that maps each of our two services to different hosts:
```
kubectl create ingress demo-ingress --class=nginx \
  --rule="demo1.localdev.me/*=demo-service1:80" \
  --rule="demo2.localdev.me/*=demo-service2:80"
```

the following command forwards a local port to the ingress controller
```
# port forwarding
kubectl port-forward --namespace=ingress-nginx service/ingress-nginx-controller 8080:80
```

and we can see them communicating to the different images using this command:
```
curl http://demo1.localdev.me:8080/
curl http://demo2.localdev.me:8080/
```

to configure the load balancer to serve over an external IP:
```
kubectl patch svc ingress-nginx-controller -n ingress-nginx -p '{"spec": {"type": "LoadBalancer", "externalIPs":["172.31.71.218"]}}'
```
verify that the "EXTERNAL-IP" field is not pending when you run:
```
kubectl get service ingress-nginx-controller --namespace=ingress-nginx
```

## Trevor's next steps
- looking into SSL termination utilizing this ingress resource
- eventually, connecting to OAuth


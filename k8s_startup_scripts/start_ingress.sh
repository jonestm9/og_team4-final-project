#!/bin/bash

# Install Ingress-Nginx
helm upgrade --install ingress-nginx ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace ingress-nginx --create-namespace

# Wait for Ingress-Nginx controller pod to be ready
kubectl wait --namespace ingress-nginx \
  --for=condition=ready pod \
  --selector=app.kubernetes.io/component=controller \
  --timeout=120s
  
# Create secret using our generated files
kubectl create secret tls demo-tls-secret --namespace ingress-nginx \
  --cert=demo-tls-cert.pem --key=demo-tls-key.pem

# Create demo-service1 deployment and expose it
kubectl create deployment demo-service1 --image=httpd --port=8081
kubectl expose deployment demo-service1 --port=80

# Create demo-service2 deployment and expose it
kubectl create deployment demo-service2 --image=nginx --port=8082
kubectl expose deployment demo-service2 --port=80

# Create Ingress for demo-service1 and demo-service2
kubectl create ingress demo-ingress --class=nginx \
  --rule="demo1.localdev.me/*=demo-service1:80" \
  --rule="demo2.localdev.me/*=demo-service2:80"

# Port forwarding for Ingress-Nginx
kubectl port-forward --namespace=ingress-nginx service/ingress-nginx-controller 8080:80 &

# Wait for port forwarding to be ready
sleep 5

# Patch Ingress-Nginx service to use LoadBalancer with external IP
kubectl patch svc ingress-nginx-controller -n ingress-nginx -p '{"spec": {"type": "LoadBalancer", "externalIPs":["172.31.71.218"]}}'

# Display Ingress-Nginx service details
kubectl get service ingress-nginx-controller --namespace=ingress-nginx

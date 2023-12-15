Follow the steps on this webpage linked below to implement the external OAuth authentication of the ingress controller on your device. You should do this AFTER creating and testing the ingress controller and load balancer.
https://kubernetes.github.io/ingress-nginx/examples/auth/oauth-external-auth/


Note: In step 4 of the implementation, you are asked to replace __INGRESS_HOST__ with a valid FQDN and __INGRESS_SECRET__ with a Secret with a valid SSL certificate. Use the external IP address of the load balancer as the FQDN. Run the commands under "TLS certificates" to create the TLS secret, then use the name you used in the command to replace __INGRESS_SECRET__.

The TLS certificate command can be found here:
https://kubernetes.github.io/ingress-nginx/examples/PREREQUISITES/



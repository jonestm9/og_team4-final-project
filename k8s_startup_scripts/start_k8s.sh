# !/bin/sh
#
# Shell script to start a kubernetes cluster locally on our VM with just one
# machine serving as both a master and worker

# make sure swap is turned off
echo "turning swap off"
sudo swapoff -a

# start cluster
echo "Starting the cluster"
sudo kubeadm init --pod-network-cidr=10.244.0.0/16

# create the directory
echo "Creating the ~/.kube and copying config file"
mkdir -p ${HOME}/.kube
sudo cp -i /etc/kubernetes/admin.conf ${HOME}/.kube/config
sudo chown $(id -u):$(id -g) ${HOME}/.kube/config

# restart containerd and maybe docker to get the K8s to really work.
echo "Restarting containerd and docker"
sudo systemctl restart containerd.service
sudo systemctl restart docker.service

# install Flannel CNI
echo "Apply flannel"
kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml

# make the master also behave as worker
echo "Taint the master so it can serve as a worker"
kubectl taint nodes trevor-virtualbox node-role.kubernetes.io/control-plane:NoSchedule-



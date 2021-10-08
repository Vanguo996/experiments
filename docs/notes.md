

部署单节点的kubernetes

k8s集群的单机部署

添加国内源
```
cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=http://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=0
repo_gpgcheck=0
gpgkey=http://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg
              http://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
EOF
```


```
WARNING Firewalld]: firewalld is active, please ensure ports [6443 10250] are open or your cluster may not function correctly
```

开启防火墙
```
// 6443
firewall-cmd --zone=public --add-port=6443/tcp --permanent && firewall-cmd --reload
// 10250
firewall-cmd --zone=public --add-port=10250/tcp --permanent && firewall-cmd --reload
```

下载镜像：

```
for i in `kubeadm config images list`; do 
imageName=${i#k8s.gcr.io/}
docker pull registry.aliyuncs.com/google_containers/$imageName
docker tag registry.aliyuncs.com/google_containers/$imageName k8s.gcr.io/$imageName
docker rmi registry.aliyuncs.com/google_containers/$imageName
done;
```
从阿里云下载镜像，重新命名




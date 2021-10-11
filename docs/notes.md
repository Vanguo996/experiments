



## 部署单节点的kubernetes

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


永久关闭swap分区


为什么关闭swap分区，swap启用后磁盘空间和内存空间交换数据的时候性能会下降。

kubelet在1.9版本之后强制要求swap关闭

查看swap当前的状态：

```
free -m
```

临时关闭：

```
swapoff -a
```


永久关闭swap：

```
vim /etc/fstab

注释掉#/dev/mapper/cl-swap     swap                    swap    defaults        0 0
```


初始化完成之后：
安装插件
```
kubectl apply -f "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')"
```


把主节点加入工作负载，开机单机模式：
```
kubectl taint node vanserver node-role.kubernetes.io/master
```


## dashboard配置

curl https://raw.githubusercontent.com/kubernetes/dashboard/v2.2.0/aio/deploy/recommended.yaml

暴露端口

```yaml
kind: Service
apiVersion: v1
metadata:
  labels:
    k8s-app: kubernetes-dashboard
  name: kubernetes-dashboard
  namespace: kubernetes-dashboard
spec:
  type: NodePort
  ports:
    - port: 443
      targetPort: 8443
      nodePort: 30001
  selector:
    k8s-app: kubernetes-dashboard
```


api server认证
创建ServiceAccount对象
```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: admin # sa名称与rolebinding一致
  namespace: kubernetes-dashboard
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: admin
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: admin
  namespace: kubernetes-dashboard
```

kubectl get svc -A

获取进入dashborad的token
```
kubectl -n kubernetes-dashboard describe secret $(kubectl -n kubernetes-dashboard get secret | grep admin | awk '{print $1}')
```


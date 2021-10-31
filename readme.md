
docs

- containerization 仪器测量容器化的相关文件


## 容器化测量服务

- 先在宿主机中安装模块(module)即ni-visa驱动，

- dkms更新模块，使得宿主机能够与仪器通信。

- 容器共享宿主机的内核，同样就可以共享内核的模块，docker在运行的时候挂载dkms相关的目录，以及`lib/modules`

创建一个测试的命名空间：

> 命名空间的作用：隔离资源，允许某些特定用户访问资源，限制单个用户可用的计算资源量。

```
kubectl create namespace visa-expirements
```

k8s中运行第一个应用

部署前端应用

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name:  demo-react
  namespace: default
  labels:
    app: demo-react
spec:
  selector:
    matchLabels:
      app: demo-react
  replicas: 1
  strategy:
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 25%
    type: RollingUpdate
  template:
    metadata:
      labels:
        app: demo-react
    spec:
      containers:
      - name:   demo-react
        image:  vanguo996/demoreact
        ports:
        - containerPort:  3000
          name:   demo-react
```

部署应用对应的service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: demo-react-nodeport
  namespace: default
spec:
  type: NodePort
  ports:
  - port: 80
    targetPort: 3000
    nodePort: 30123
  selector:
    app: demo-react
```


可以看到已经运行在30123端口
```
$ kubectl get svc -A 
NAMESPACE              NAME                        TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                  AGE
default                demo-react-nodeport         NodePort    10.104.4.233     <none>        80:30123/TCP             3h5m
```

容器化仪器测量应用在k8s中的部署



## 部署k8s

重新部署k8s：

- 重置k8s出现问题：
https://www.codenong.com/js31f7dda9ccf7/


rm -rf /etc/kubernetes/*
rm -rf /root/.kube/


docker run -d \
  --restart=unless-stopped \
  --name=kuboard \
  -p 80:80/tcp \
  -p 10081:10081/tcp \
  -e KUBOARD_ENDPOINT="http://192.168.1.101:80" \
  -e KUBOARD_AGENT_SERVER_TCP_PORT="10081" \
  -v /root/kuboard-data:/data \
  eipwork/kuboard:v3




cat > /etc/sysctl.d/k8s.conf << EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
sysctl --system  


apiVersion: kubeadm.k8s.io/v1beta2
kind: ClusterConfiguration
kubernetesVersion: v1.18.5
imageRepository: "registry.aliyuncs.com/google_containers"
networking:
  podSubnet: 10.100.0.0/16

kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml



master节点安装了kubelet，默认情况下不参与工作负载，使master节点也参与workload：

```
kubectl taint node van-master node-role.kubernetes.io/master-
```



安装集群


```

# 在 master 节点和 worker 节点都要执行
# 最后一个参数 1.21.5 用于指定 kubenetes 版本，支持所有 1.21.x 版本的安装
# 腾讯云 docker hub 镜像
# export REGISTRY_MIRROR="https://mirror.ccs.tencentyun.com"
# DaoCloud 镜像
# export REGISTRY_MIRROR="http://f1361db2.m.daocloud.io"
# 华为云镜像
# export REGISTRY_MIRROR="https://05f073ad3c0010ea0f4bc00b7105ec20.mirror.swr.myhuaweicloud.com"
# 阿里云 docker hub 镜像
export REGISTRY_MIRROR=https://registry.cn-hangzhou.aliyuncs.com
curl -sSL https://kuboard.cn/install-script/v1.21.x/install_kubelet.sh | sh -s 1.21.5

```


```
# 只在 master 节点执行
# 替换 x.x.x.x 为 master 节点实际 IP（请使用内网 IP）
# export 命令只在当前 shell 会话中有效，开启新的 shell 窗口后，如果要继续安装过程，请重新执行此处的 export 命令
export MASTER_IP=192.168.1.101
# 替换 apiserver.demo 为 您想要的 dnsName
export APISERVER_NAME=apiserver.demo
# Kubernetes 容器组所在的网段，该网段安装完成后，由 kubernetes 创建，事先并不存在于您的物理网络中
export POD_SUBNET=10.100.0.0/16
echo "${MASTER_IP}    ${APISERVER_NAME}" >> /etc/hosts
curl -sSL https://kuboard.cn/install-script/v1.21.x/init_master.sh | sh -s 1.21.5 /coredns

```

安装网络插件

```
export POD_SUBNET=10.100.0.0/16
kubectl apply -f https://kuboard.cn/install-script/v1.21.x/calico-operator.yaml
wget https://kuboard.cn/install-script/flannel/flannel-v0.14.0.yaml
sed -i "s#10.244.0.0/16#${POD_SUBNET}#" flannel-v0.14.0.yaml
kubectl apply -f ./flannel-v0.14.0.yaml
```
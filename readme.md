
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



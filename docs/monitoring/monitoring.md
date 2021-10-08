
promethus

- 易于管理，只有一个单独的二进制文件，
- 使用pull模型可以在任何地方搭建监控系统
- 所有监控数据以指标的形式保存在**时间序列数据库**

- 能够高效的处理数以百万的指标，
- 秒处理十万的数据点


## promethus的安装
```
git clone https://github.com/coreos/kube-prometheus.git
```

1. 其中创建CRD资源
```
kubectl apply -f kube-prometheus/manifests/setup/
kubectl get crd |grep monitoring
```


2. 部署了prometheus-operator的dep和svc

```
kubectl get deployments -n monitoring
kubectl get services -n monitoring
```

3. 部署prometheus其他组件，包含kube-state-metric，grafana，node-exporter，alertmanager，prometheus-adapter，prometheus，组件包含在manifest所在目录，安装组件的角色如下：

- prometheus                prometheus核心组件
- prometheus-adapter   prometheus适配器，做数据转换
- kube-state-metrics    kubernetes指标转换器，转换为apiserver能识别的指标
- alertmanager             告警管理器，用于指标阀值告警实现
- node-exporter           exporters，客户端监控上报agent，用于实现数据上报
- grafana                    数据显示展板
- configmaps              grafana数据展板配置模版，封装在configmap中
- clusterrole，clusterrolebinding    prometheus访问kubernetes的RBAC授权 


```
kubectl apply -f kube-prometheus/manifests/
```


校验prometheus安装情况，包括node-exporter、kube-state-metrics、prometheus-adapter、alertmanager、grafana等

kubectl get daemonsets -n monitoring 

kubectl get pods -n monitoring  |grep node-exporter

- prometheus-adapter，grafana，kube-state-metrics以deployments的形式部署

kubectl get deployments -n monitoring

- prometheus核心组件和告警组件，以statefulsets的形式部署

kubectl get statefulsets.apps -n monitoring 

- 服务暴露，包括grafana，prometheus等


## promethus的使用

promethus组件的暴露使用

kubectl get services -n monitoring prometheus-k8s -o yaml

```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    app.kubernetes.io/component: prometheus
    app.kubernetes.io/name: prometheus
    app.kubernetes.io/part-of: kube-prometheus
    app.kubernetes.io/version: 2.30.2
    prometheus: k8s
  name: prometheus-k8s
  namespace: monitoring
spec:
  ports:
  - name: web
    nodePort: 31924
    port: 9090
    targetPort: web
  # - name: reloader-web
  #   port: 8080
  #   targetPort: reloader-web`
  selector:
    app: prometheus
    app.kubernetes.io/component: prometheus
    app.kubernetes.io/name: prometheus
    app.kubernetes.io/part-of: kube-prometheus
    prometheus: k8s
  sessionAffinity: ClientIP
  type: NodePort
status:
  loadBalancer: {}


```

grafana组价的暴露


```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    app.kubernetes.io/component: grafana
    app.kubernetes.io/name: grafana
    app.kubernetes.io/part-of: kube-prometheus
    app.kubernetes.io/version: 8.1.5
  name: grafana
  namespace: monitoring
spec:
  ports:
  - name: http
    nodePort: 31925
    port: 3000
    targetPort: http
  selector:
    app.kubernetes.io/component: grafana
    app.kubernetes.io/name: grafana
    app.kubernetes.io/part-of: kube-prometheus
  type: NodePort
status:
  loadBalancer: {} 

```
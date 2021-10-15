本实验旨在实现 容器化的测量服务与仪器之间的通信。

## 容器化测量服务

示意图：

<img src=https://tva1.sinaimg.cn/large/008i3skNgy1gu8ygd0juzj60my0yc41g02.jpg width = "300" height = "500" alt="图片名称" align=center />


pod中的visa库通过`远程资源名称`与虚拟仪器服务器(Measurement Server)进行通信。

在建立通信之前，需要在容器中安装ni-visa库。

## 容器化仪器测量原理：

- 容器中的visa lib通过session获取到ResourceManager，资源管理器。

- 资源管理器访问visa系统，通过资源操作来访问`容器外`的测量服务器，即虚拟仪器服务器


## 制作一个visa lib镜像

关键技术: 在centos容器中安装visa驱动，

> 驱动支持的操作系统：https://www.ni.com/pdf/manuals/378353a.html


```
安装​存储​库​附件：
sudo yum install <.rpm file name>
​示例：
sudo yum install ni-​software-2020-20.1.0.49152-0+f0.el7.noarch.rpm

使用​Linux​的​程序​包​管理​器，​下载​并​安装​驱动​程序​包。​软件​包​名称​可在​NI Linux Device Drivers​自述​文件​中​找到。
sudo yum install <package name>
​示例：
sudo yum install ni-​daqmx

更新​内​核：
sudo dkms autoinstall

重​启​系统。

```


dkms autoinstall问题
```
Error! echo
Your kernel headers for kernel 3.10.0-1160.41.1.el7.x86_64 cannot be found at
/lib/modules/3.10.0-1160.41.1.el7.x86_64/build or /lib/modules/3.10.0-1160.41.1.el7.x86_64/source.
```

## 关于内核模块的注意事项

linux的模块机制：内核在初始化的时候就是初始化很多模块，

- 内核模块保存在`/lib/modules/<kernel_version>/kernel`，

- depmod 会自动扫描系统中的所有模块生成`modules.dep`文件

- lsmod查看内核中所有的模块

docker容器共享内核，那么驱动只要安装在宿主机上，容器就可以使用宿主机的驱动吗？

但是在容器中运行连接仪器的程序时，显示缺少驱动

```shell
python3 test.py

libnipalu.so failed to initialize
Verify that nipalk.ko is built and loaded.
Aborted (core dumped)

```

在容器中执行lsmod
```
Module                  Size  Used by
NiViPciK               81344  1 
nimru2k               772013  1 
nipxirmk              304763  1 
nimxdfk               592969  3 nimru2k
nimdbgk               469751  5 nipxirmk,nimru2k,nimxdfk
nidimk                377043  4 nipxirmk,nimru2k
niorbk                125271  5 nipxirmk,nimdbgk,nimru2k,nimxdfk,nidimk
ni488k                205909  0 
nipalk               1253264  12 nipxirmk,NiViPciK,nimdbgk,nimru2k,nimxdfk,ni488k,nidimk,niorbk
nikal                 117817  7 nipxirmk,nimdbgk,nimru2k,nimxdfk,nidimk,nipalk,niorbk
```

表明在容器中执行lsmod显示的为宿主机中的模块





### dkms作用

DKMS全称是DynamicKernel ModuleSupport，它可以帮我们维护内核外的驱动程序

如果需要使用没有集成到内核中的linux驱动，需要手动编译，

linux模块和内核有依赖关系，如果因为发行版本的更新导致内核版本变动，

之前编译的模块需要重新编译，为了避免这样的问题，dkms可以帮助开发者维护内核之外的驱动程序

其中安装驱动的过程图：
![](../images/dkms.png)

dkms管理内核的模块，其中需要满足两个要求

- 源码存放在/usr/src/对应的modules-name目录下，

```
[root@d7d1d9a5a282 src]# ls
debug  kernels  nikal-20.0.0f0  nipalk-20.0.0f0  NiViPciK-20.0.0f0
[root@d7d1d9a5a282 src]# pwd
/usr/src
```

- 源码目录中要有dkms.conf文件

在安装ni-visa之后，其中三个模块已经是加载状态。
```
dkms status
nikal, 20.0.0f0: added
nipalk, 20.0.0f0: added
NiViPciK, 20.0.0f0: added
```

下一步构建模块：
```
dkms build nikal/20.0.0f0
Error! echo
Your kernel headers for kernel 3.10.0-1160.41.1.el7.x86_64 cannot be found at
/lib/modules/3.10.0-1160.41.1.el7.x86_64/build or /lib/modules/3.10.0-1160.41.1.el7.x86_64/source.
```

/lib/modules中创建符号链接
ln -s /usr/src/kernels/3.10.0-1160.41.1.el7.x86_64 build

再次构建：

```
dkms build nikal/20.0.0f0
成功
```

```
dkms status
nikal, 20.0.0f0, 3.10.0-1160.41.1.el7.x86_64, x86_64: installed
nipalk, 20.0.0f0: added
NiViPciK, 20.0.0f0: added
```

安装成功的模块会在以下文件中找到：

updatedb
locate nikal.ko

```
/usr/lib/modules/3.10.0-1160.41.1.el7.x86_64/extra/nikal.ko
/var/lib/dkms/nikal/20.0.0f0/3.10.0-1160.41.1.el7.x86_64/x86_64/module/nikal.ko

```

安装剩下的模块：

```
dkms build nipalk/20.0.0f0

dkms build NiViPciK/20.0.0f0

都出现类似的错误：
Kernel preparation unnecessary for this kernel.  Skipping...
Building module:
cleaning build area...
make -j4 KERNELRELEASE=3.10.0-1160.41.1.el7.x86_64 KERNELDIR=/lib/modules/3.10.0-1160.41.1.el7.x86_64/build KERNELVER=3.10.0-1160.41.1.el7.x86_64 build...(bad exit status: 2)
Error! Bad return status for module build on kernel: 3.10.0-1160.41.1.el7.x86_64 (x86_64)
Consult /var/lib/dkms/NiViPciK/20.0.0f0/build/make.log for more information.
```


查看日志：
```
Making nipalk.ko
  SHIPPED /var/lib/dkms/nipalk/20.0.0f0/build/nipalk-bin.o
  CC [M]  /var/lib/dkms/nipalk/20.0.0f0/build/nipalk-interface.o
/bin/sh: line 1:  4477 Killed                  ./tools/objtool/objtool check "/var/lib/dkms/nipalk/20.0.0f0/build/nipalk-interface.o"
make[2]: *** [/var/lib/dkms/nipalk/20.0.0f0/build/nipalk-interface.o] Error 137
make[1]: *** [_module_/var/lib/dkms/nipalk/20.0.0f0/build] Error 2
make: *** [nipalk.ko] Error 2


more /var/lib/dkms/NiViPciK/20.0.0f0/build/make.log
DKMS make.log for NiViPciK-20.0.0f0 for kernel 3.10.0-1160.41.1.el7.x86_64 (x86_64)
Mon Oct  4 07:12:32 UTC 2021
make: *** No rule to make target `/var/lib/nikal/3.10.0-1160.41.1.el7.x86_64/symvers/nipalk.symvers', needed by `NiViPciK.ko'.  Stop.
```



### 什么是kernel modules

什么是kernel？

kernel是应用程序和cpu、内存和设备之间沟通的桥梁，也是操作系统的核心

<img src=https://tva1.sinaimg.cn/large/008i3skNgy1gv3254bw8kj60jw0fk3z502.jpg width = "300" height = "300" alt="图片名称" align=center />

linux的内核时模块化组成的，内核在运行时可以动态地插入或者删除代码，这些代码被称为**可装载的内核模块**，这样的好处是：基本内核可以做到很小。

内核模块(kernel modules)：



## docker container loading kernel modules

在centos容器中执行lsmod，其中显示有ni-visa相关的模块，

现在问题是容器中如何加载内核中的模块？

- run container in privileage mode  特权容器拥有所有的capabilities

- add all capabilities  添加权限

- mount host /lib/modules into container

什么是容器的`capabilities`? 权限

容器通过系统调用来与内核进行交互，其中不包括与任何容器内核模块的交互，这就是为什么容器被设计为轻量化的原因。


共享库：
```
docker run --name visa-test --privileged --cap-add ALL -it 
-v /lib/modules:/lib/modules 
-v /var/lib/dkms:/var/lib/dkms 
-v /usr/src:/usr/src 
vanguo996/centos-pyvisa:v2
```

运行dkms：
```
[root@e9bb32c66d80 app]# dkms status
NiViPciK/20.0.0f0, 3.10.0-1160.el7.x86_64, x86_64: installed
nikal/20.0.0f0, 3.10.0-1160.el7.x86_64, x86_64: installed
nipalk/20.0.0f0, 3.10.0-1160.el7.x86_64, x86_64: installed
```
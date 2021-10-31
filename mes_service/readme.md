# 6221 measurements

## 6221 source current

用于产生单个电流节点。




```

CLEar ‘ Turns the output off.
CURRent:RANGe:AUTO ON ‘ Enables autorange.
CURRent 12e-3 ‘ Sets output level to +12mA.
CURRent:COMPliance 10 ‘ Sets voltage compliance to 10V.
OUTPut ON ‘ Turns the output on.
OUTPut OFF ‘ Turns the output off

```



## 6221 sweep operation
可以产生扫描电流，

```
instr1.write('*RST')
instr1.write('SOUR:CURR 1e-4')
instr1.write('SOUR:CURR:COMP 10')
instr1.write('SOUR:SWE:SPAC LIN')
instr1.write('SOUR:CURR:STAR 1e-3')
instr1.write('SOUR:CURR:STOP 1e-2')
instr1.write('SOUR:CURR:STEP 1e-3')
instr1.write('SOUR:DEL 1') 
instr1.write('SOUR:SWE:')

```

## 6221 delta/pulse delta operation

6221产生双极性电流，2182进行AD转换，测量。并且使用平均算法来计算数据

 - delta，6221提供方形电流脉冲，2182分别在高或低水平测量，

 两者通信方式为  RS232 and TRIG 








# 2182A measurements

## simple voltage measurement

```
:SENSe
 :FUNCtion <name> Select function: ‘VOLTage’ or ‘TEMPerature’.  default: VOLT
 :CHANnel <chan>  Select measurement channel: 0, 1 or 2 (see Note).   default: 1
 :DATA Return 2182 readings: 
 [:LATest]? Return the last reading.
 :FRESh?

```

依据以上说明，第一个demo：

```
from gpib_ctypes import make_default_gpib
make_default_gpib()
import visa
import time

rm = visa.ResourceManager("@py")
instr6221 = rm.open_resource('GPIB0::7::INSTR')
instr2182A = rm.open_resource('GPIB::8::INSTR')

instr6221.write('cle')
instr6221.write('curr:rang:auto on')
instr6221.write('curr 10e-3')
instr6221.write('curr:compliance 10')
instr6221.write('outp on')

i = 30
while i:
    data = instr2182A.query(':sens:data:fres?')
    print(data)
    i -= 1

instr6221.write('outp off')
```

但此时2182测量速度较慢，需要调整速度
说明书中表14-7，显示了所有2182的命令    

```
:sens  #第一级命令
    :volt  #第二级命令表示 配置直流电压
        :NPLC 【默认为 5】#第三级命令表示 设置速度 
```



实验：

    测量一个100k的电阻，不用trig，使用6221电流表产生电流，使用2182A测量电压。

    电流0.1mA - 电压9.9v
    电流1mA - 电压99v 但此时2182A显示为19v，此时链接的是CH1 理论上最大是120v

默认为CH1，但此时测量到99v，只显示19v

注意：在6221中设置了保护电压，20v


## 2182A - Range,Digits,Rate,Filter

1. 设置范围：
    
```
:SENSe:
 :VOLTage
 [:CHANnel1] Channel 1 (DCV1):
 :RANGe    Range selection: 
 [:UPPer] <n>  Specify expected reading: 0 to 120 (volts). default 120
 : AUTO <b>  Enable or disable auto range.

```
python代码：
```
instr2182A.write(':sens:volt:rang:auto on'
```



2. 设置Digits
    digits resolution 4 - 8  分别表示 不同的精度 默认下为最高精度

3. 设置range



## speed

    nplc 1  读取速度为  0.05 - 0.07
    nplc 0.1 读取速度为 0.02 - 0.03



# 








# 数据可视化
    

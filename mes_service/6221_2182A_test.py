from gpib_ctypes import make_default_gpib
make_default_gpib()
import visa
import time
import data_visuallization
"""
    6221产生电流
        设置高度
        设置保护电压
    2182测电压
        设置测量速度
        设置范围


"""



rm = visa.ResourceManager("@py")
instr6221 = rm.open_resource('GPIB0::7::INSTR')
instr2182A = rm.open_resource('GPIB::8::INSTR')

instr6221.write('cle')
instr6221.write('curr:rang:auto on')
instr6221.write('curr 1e-4')
instr6221.write('curr:compliance 100')

instr2182A.write(':sens:volt:nplc 1')
instr2182A.write(':sens:volt:rang:auto on') # error 110  cmd header error

instr6221.write('outp on')

i = 30
while i:
    start_time = time.time()
    data = instr2182A.query(':sens:data:fres?')
    end_time = time.time()
    print(data)
    print("time is ： %s" % (end_time - start_time) )
    i -= 1

instr6221.write('outp off')
instr2182A.write('*rst')



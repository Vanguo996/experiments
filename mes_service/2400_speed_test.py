from gpib_ctypes import make_default_gpib
make_default_gpib()
import pyvisa as visa
import time

rm = visa.ResourceManager('@py')
instr1 = rm.open_resource('GPIB0::24::INSTR')
instr1.write('*rst')
instr1.write(':sour:func "curr"')
instr1.write(':sens:func "volt"')
instr1.write(':sour:curr:lev 1e-8')
instr1.write(':sens:volt:nplc 1')
instr1.write(':outp on')

# instr1.write('func "res"')
# instr1.write('res:mode auto')
# instr1.write('res:rang 20e6')
# instr1.write(':syst:rsen on')
# instr1.write(':form:elem res')
# instr1.write('outp on')




# i = 5
# while(i):
#     start_time = time.time()
#
#     data = instr1.query(':read?')
#     end_time = time.time()
#     print(end_time - start_time)
#     i -= 1


j = 100
while(j):
    start_time1 = time.time()
    # instr1.write(':init')
    data1 = instr1.query(':read?')
    print(data1)

    end_time1 = time.time()
    print(end_time1 - start_time1)
    j -= 1



instr1.write(':outp off')













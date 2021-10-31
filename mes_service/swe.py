import pyvisa as visa
import csv
import time
import multiprocessing
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation


class mes:


    def __init__(self):

        self.a = -2

        self.b = 2

        self.c = 0.01

        self.cmpl = 100e-3


        self.directory = '6221'

        self.file = '3'

        self.filename = '{}/{}.csv'.format(self.directory, self.file)

    def initial_csv_62(self):
        feildname = ['voltage', 'current', 'none', 'time', 'res']
        with open(self.filename, 'w') as file2:
            csv_writer = csv.DictWriter(file2, fieldnames=feildname)
            csv_writer.writeheader()

    def animate(self, i):
        data1 = pd.read_csv('%s' % self.filename)
        x = data1['voltage']
        y = data1['current']
        z = data1['res']
        self.ax1.cla()
        self.ax2.cla()
        self.ax1.plot(x, y, marker='o', label='V-I')
        self.ax2.plot(z, marker='*', label='resistance')

        self.ax1.set_xlabel('voltage')
        self.ax1.set_ylabel('current')
        self.ax2.set_xlabel('voltage')
        self.ax2.set_ylabel('resistance')
        self.ax1.legend()
        self.ax2.legend()

    def live_plot(self):
        fig = plt.figure(figsize=(13, 6))
        plt.style.use('ggplot')
        self.ax1 = fig.add_subplot(121)
        self.ax2 = fig.add_subplot(122)
        self.ax1.cla()
        self.ax2.cla()
        ani = FuncAnimation(fig, self.animate, interval=100)
        plt.show()

    def sweep_mode(self):
        rm = visa.ResourceManager()
        instr = rm.open_resource('visa://202.197.78.43/GPIB0::24::INSTR')
        instr.write('*rst')
        instr.write(':outp on')
        instr.write(':sour:func volt')
        instr.write(':sens:curr:prot %s' % self.cmpl)
        instr.write(':sens:func "curr:dc"')
        instr.write(':sens:nplc 5cc')
        instr.write(':trig:coun 1')
        instr.write(':trig:del 0')
        instr.write(':sour:del 0')
        
        i = self.a
        flag = True
        while (flag):
            instr.write(':sour:volt:lev %s' % i)
            data = instr.query('read?')
            list_data = data.split(',')
            list_data.pop()
            resistance = float(list_data[0])/float(list_data[1])

            list_data.append('%s\n' % resistance)

            data1 = ','.join(list_data)
            print(data1)

            with open('%s' % self.filename, 'a') as file:
                file.write(data1)

            i += self.c

            x = int(i)
            print(x)

            if round(x, 2) == self.b:
                flag = False
                instr.write(':outp off')

if __name__ == "__main__":
    temp = mes()
    temp.initial_csv_62()
    t1 = multiprocessing.Process(target=temp.sweep_mode, )
    t2 = multiprocessing.Process(target=temp.live_plot, )

    t1.start()
    t2.start()

    t1.join()
    t2.join()
























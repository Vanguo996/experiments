from data_gen import data_gen
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import pandas as pd


class data_plot:
    def __init__(self):
        self.s1 = data_gen() # init file
        self.filename = self.s1.filename
        self.ax1 = None

    def plot(self):
        plt.style.use("ggplot")
        fig = plt.figure()
        self.ax1 = fig.add_subplot()
        ani = FuncAnimation(fig, self.animate, interval=1000, repeat=True)
        plt.show()

    def animate(self, i):
        data = pd.read_csv(self.filename)
        x = data['time']
        y = data['value1']
        z = data['value2']
        self.ax1.cla()
        self.ax1.plot(x, y, z, label='time-value1', marker='*')






from simulation import data_plot
from simulation import data_gen


from multiprocessing import Process

class main:

    def __init__(self):
        gen = data_gen.data_gen()
        p = data_plot.data_plot()
        p.filename = gen.filename

        self.t1 = Process(target=gen.generate)
        self.t2 = Process(target=p.plot)

    def run(self):
        self.t1.start()
        self.t2.start()

    def stop(self):
        self.t1.terminate()
        self.t2.terminate()


if __name__ == '__main__':
    main().run()
        


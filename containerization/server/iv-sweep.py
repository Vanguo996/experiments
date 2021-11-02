# coding=utf-8

import time
import pyvisa as visa
import logging

# from conn import ConnectionTest
import config

class SweepTest():

    def __init__(self):
        self.rm = visa.ResourceManager(config.visa_lib)
        logging.info("资源管理器初始化完成")
        self.instr2400 = self.rm.open_resource(config.instr_2400)
        logging.info("打开资源：%s", config.instr_2400)
        instr_info = self.instr2400.query("*idn?")
        logging.info(instr_info)


    def instr_init(self):
        """初始化2400

        """
        self.instr2400.write("*rst?")
        # 关闭蜂鸣器
        self.instr2400.write(":syst:beep:stat off")

        # error_queue = self.instr2400.query(":syst:error?")
        # logging.info(error_queue)


    def ohm_mes(self):
        """
        FUNC “RES”
        RES:MODE AUTO
        RES:RANG 20E3    20k ohm
        :SYST:RSEN ON  四线测量
        :FORM:ELEM RES
        :OUTP ON
        :READ?
        :OUTP OFF
        """

        self.instr_init()
        self.instr2400.write('func "res"')
        self.instr2400.write('res:mode auto')
        self.instr2400.write('res:rang 20e6')
        self.instr2400.write(':form:elem res')
        self.instr2400.write(':outp on')

        # tmp = self.instr2400.query(":read?")
        # logging.info(tmp)

        # self.instr2400.write(':outp off')
        
        i = 10
        while i:    
            tmp = self.instr2400.query(":read?")
            print(tmp)
            i -= 1
            time.sleep(1)
        self.instr2400.write(':outp off')


    def sweep_source_v(self, 
        start_volt: int, 
        end_volt: int, 
        volt_step: float, 
        current_cmpl: float):
        """source v, measure i
        
        use basic source-measure operation simulate the real-time sweeep mode  


        Parameters
        ----------

        """

        self.instr_init()

        self.instr2400.write("sour:func volt")
        self.instr2400.write(':sens:curr:prot %s' % current_cmpl)
        self.instr2400.write(':sens:func "curr:dc"')
        self.instr2400.write(':sens:nplc 5')
        self.instr2400.write(':trig:coun 1')
        self.instr2400.write(':trig:del 0')
        self.instr2400.write(':sour:del 0')
        # 时间戳重置
        self.instr2400.write(':syst:time:res:auto off')
        # 查看是否
        # self.instr2400.write('')
        
        
        self.instr2400.write(':outp on')

        source_volt_level = start_volt

        while 1:
            self.instr2400.write(':sour:volt:lev %s' % (source_volt_level))
            measure_i_info = self.instr2400.query(':read?')
            
            print(type(measure_i_info))

            source_volt_level += volt_step
            source_volt_level = round(source_volt_level, 10)
            if source_volt_level == end_volt:
                break




if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s",
                    datefmt = '%Y-%m-%d %H:%M:%S %a'   
                    )

    st = SweepTest()

    # 获取电阻值
    # st.ohm_mes()

    st.sweep_source_v(-2, 2, 0.1, 100e-3)


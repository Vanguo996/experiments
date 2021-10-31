# coding=utf-8

import pyvisa as visa
import logging

# from conn import ConnectionTest
import config

class SweepTest():

    def __init__(self):
        self.rm = visa.ResourceManager(config.visa_lib)
        logging.info("资源管理器初始化完成")

    def get_instr_name(self):
        instr2400 = self.rm.open_resource(config.instr_2400)
        instr_info = instr2400.query("*idn?")
        logging.info(instr_info)



    



if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(name)s %(levelname)s %(message)s",
                    datefmt = '%Y-%m-%d  %H:%M:%S %a'    #注意月份和天数不要搞乱了，这里的格式化符与time模块相同
                    )

    st = SweepTest()
    st.get_instr_name()


    
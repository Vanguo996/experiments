import pyvisa as visa
import time

import config

class ConnectionTest():

    def __init__(self):
        self.rm = visa.ResourceManager("@ivi")
        print(self.rm)

    def connection_test(self, resource_name):    
        # instr = rm.open_resource("visa://192.168.1.108/GPIB0::7::INSTR")
        instr = self.rm.open_resource(resource_name)
        return instr


    def visalib_test():
        rm = visa.ResourceManager("@ivi")
        print(rm)

    def list_all_instruments(self):
        """
        """
        print(self.rm.list_resources())


if __name__ == "__main__":
    
    ct = ConnectionTest()
    while 1:
        ct.list_all_instruments()
        instr = ct.connection_test(config.test_instr_name)
        print(instr)
        time.sleep(1)
        
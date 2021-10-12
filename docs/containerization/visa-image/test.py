import pyvisa as visa
import time


class ConnectionTest():

    def __init__(self):
        self.rm = visa.ResourceManager()

    def connection_test(self, resource_name):    
        # instr = rm.open_resource("visa://192.168.1.108/GPIB0::7::INSTR")
        instr = self.rm.open_resource(resource_name)
        print("找到仪器：", instr)


    def visalib_test():
        rm = visa.ResourceManager("@ivi")
        print(rm)

    def list_all_instruments(self):
        """
        """
        print(self.rm.list_resources())


if __name__ == "__main__":
    
    ct = ConnectionTest()
    test_name = "visa://202.197.78.43/GPIB0::INTFC"
    while 1:
        ct.list_all_instruments()
        ct.connection_test(test_name)
        time.sleep(5)
        
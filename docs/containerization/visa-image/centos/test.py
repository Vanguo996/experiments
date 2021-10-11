import pyvisa as visa

def connection_test():
        
    rm = visa.ResourceManager()
    # instr = rm.open_resource("visa://192.168.1.108/GPIB0::7::INSTR")

    test_name = "visa://192.168.1.108/GPIB0::INTFC"
    instr = rm.open_resource(test_name)
    # ok = instr.query("*idn?")
    print(instr)


def visalib_test():

    rm = visa.ResourceManager("@ivi")
    print(rm)



if __name__ == "__main__":
    while i:
        connection_test()

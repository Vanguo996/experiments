import pyvisa as visa

def connection_test():
        
    rm = visa.ResourceManager()
    # instr = rm.open_resource("visa://192.168.1.108/GPIB0::7::INSTR")

    test_name = "visa://192.168.1.108/GPIB0::INTFC"
    instr = rm.open_resource(test_name)
    rm.list_resources()
    # ok = instr.query("*idn?")
    print(instr)


def visalib_test():

    rm = visa.ResourceManager("@ivi")
    print(rm)

connection_test()

# visalib_test()
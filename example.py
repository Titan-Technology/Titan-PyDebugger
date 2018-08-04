import Titan_PyDebugger
from Titan_defs import *

def main():
    debugger = Titan_PyDebugger.debugger()
    pid = input("Enter the PID of the process to attach to: ")
    debugger.attach(int(pid))
    printf_address = debugger.func_resolve("msvcrt.dll", "printf")
    print("[*] Address of printf: 0x%08x" % printf_address)
    debugger.bp_set_hw(printf_address, 1, HW_EXECUTE)
    debugger.run()
    debugger.detach()
    
main()
import simuvex

class GetCurrentProcessId(simuvex.SimProcedure):
    CALLEE_CLEANUP = True
    def run(self):
        return 0x1337BEE2

import simuvex

class QueryPerformanceCounter(simuvex.SimProcedure):
    CALLEE_CLEANUP = True
    def run(self, ptr):
        self.state.mem[ptr].qword = 0x0000005555555555
        return 1

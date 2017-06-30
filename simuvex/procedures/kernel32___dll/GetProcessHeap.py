import simuvex

class GetProcessHeap(simuvex.SimProcedure):
    CALLEE_CLEANUP = True
    def run(self):
        return 1 # fake heap handle

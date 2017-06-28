import simuvex

class GetCurrentThreadId(simuvex.SimProcedure):
    CALLEE_CLEANUP = True
    def run(self):
        return 0xbad76ead

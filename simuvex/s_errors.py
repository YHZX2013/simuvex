#
# Simulation errors
#

class SimError(Exception):
    bbl_addr = None
    stmt_idx = None
    ins_addr = None
    executed_instruction_count = None
    guard = None

    def record_state(self, state):
        self.bbl_addr = state.scratch.bbl_addr
        self.stmt_idx = state.scratch.stmt_idx
        self.ins_addr = state.scratch.ins_addr
        self.executed_instruction_count = state.history.recent_instruction_count
        self.guard = state.scratch.guard
        return self

#
# State-related errors
#

class SimStateError(SimError):
    pass

class SimMergeError(SimStateError):
    pass

class SimMemoryError(SimStateError):
    pass

class SimAbstractMemoryError(SimMemoryError):
    pass

class SimRegionMapError(SimMemoryError):
    pass

class SimMemoryLimitError(SimMemoryError):
    pass

class SimMemoryAddressError(SimMemoryError):
    pass

class SimFastMemoryError(SimMemoryError):
    pass

class SimEventError(SimStateError):
    pass

class SimFileError(SimMemoryError):
    pass

class SimPosixError(SimStateError):
    pass

#
# Error class during VEX parsing
#

class SimUnsupportedError(SimError):
    pass

#
# Solver-related errors
#

class SimSolverError(SimError):
    pass

class SimSolverModeError(SimSolverError):
    pass

class SimSolverOptionError(SimSolverError):
    pass

class SimValueError(SimSolverError):
    pass

class SimUnsatError(SimValueError):
    pass

#
# SimIROp errors
#

class SimOperationError(SimError):
    pass

class UnsupportedIROpError(SimOperationError, SimUnsupportedError):
    pass

#
# SimIRExpr errors
#

class SimExpressionError(SimError):
    pass

class UnsupportedIRExprError(SimExpressionError, SimUnsupportedError):
    pass

class SimCCallError(SimExpressionError):
    pass

class UnsupportedCCallError(SimCCallError, SimUnsupportedError):
    pass

class SimUninitializedAccessError(SimExpressionError):
    def __init__(self, expr_type, expr):
        SimExpressionError.__init__(self)
        self.expr_type = expr_type
        self.expr = expr

    def __repr__(self):
        return "SimUninitializedAccessError (expr %s is used as %s)" % (self.expr, self.expr_type)

#
# SimIRStmt errors
#

class SimStatementError(SimError):
    pass

class UnsupportedIRStmtError(SimStatementError, SimUnsupportedError):
    pass

class UnsupportedDirtyError(UnsupportedIRStmtError, SimUnsupportedError):
    pass

#
# Engine-related errors
#

class SimEngineError(SimError):
    pass

class SimIRSBError(SimEngineError):
    pass

class SimTranslationError(SimEngineError):
    pass

class SimProcedureError(SimEngineError):
    pass

class SimProcedureArgumentError(SimProcedureError):
    pass

class SimFastPathError(SimEngineError):
    pass

class UnsupportedSyscallError(SimProcedureError, SimUnsupportedError):
    pass

class SimReliftException(SimEngineError):
    def __init__(self, state):
        super(SimReliftException, self).__init__()
        self.state = state

#
# SimSlicer errors
#

class SimSlicerError(SimError):
    pass

#
# SimAction errors
#

class SimActionError(SimError):
    pass

#
# SimCC errors
#

class SimCCError(SimError):
    pass

#
# UCManager errors
#

class SimUCManagerError(SimError):
    pass

class SimUCManagerAllocationError(SimUCManagerError):
    pass

#
# SimUnicorn errors
#

class SimUnicornUnsupport(SimError):
    pass

class SimUnicornError(SimError):
    pass

class SimUnicornSymbolic(SimError):
    pass


#
# Call-stack Errors
#

class SimEmptyCallStackError(SimError):
    pass

#
# Errors that may be handled by exception handling
#

class SimException(SimError):
    pass

class SimSegfaultException(SimException, SimMemoryError):
    def __init__(self, addr, reason, original_addr=None):
        self.addr = addr
        self.reason = reason
        self.original_addr = original_addr
        super(SimSegfaultError, self).__init__('%#x (%s)' % (addr, reason))

    def __repr__(self):
        return 'SimSegfaultException(%#x (%s%s)' % (
            self.addr,
            self.reason,
            (', original %s' % self.original_addr.__repr__(max_depth=3)) if self.original_addr is not None else ''
        )

SimSegfaultError = SimSegfaultException

class SimZeroDivisionException(SimException, SimOperationError):
    pass
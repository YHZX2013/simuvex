import logging
l = logging.getLogger("simuvex.engines.procedure")

from .engine import SimEngine

#pylint: disable=unidiomatic-typecheck,arguments-differ

class SimEngineProcedure(SimEngine):
    """
    An engine for running SimProcedures
    """

    def process(self, state, procedure,
            ret_to=None,
            inline=None,
            force_addr=None):
        """
        Perform execution with a state.

        :param state:       The state with which to execute
        :param procedure:   An instance of a SimProcedure to run
        :param ret_to:      The address to return to when this procedure is finished
        :param inline:      This is an inline execution. Do not bother copying the state.
        :param force_addr:  Force execution to pretend that we're working at this concrete address
        :returns:           A SimSuccessors object categorizing the execution's successor states
        """
        return super(SimEngineProcedure, self).process(state, procedure,
                ret_to=ret_to,
                inline=inline,
                force_addr=force_addr)

    def _process(self, state, successors, procedure, ret_to=None):
        # Update state.scratch
        state.scratch.sim_procedure = procedure
        state.scratch.executed_block_count = 1

        # prepare and run!
        cleanup_options = o.AUTO_REFS not in state.options
        if cleanup_options:
            state.options.add(o.AST_DEPS)
            state.options.add(o.AUTO_REFS)

        # do it
        procedure.execute(state, successors, ret_to=ret_to)

        if cleanup_options:
            state.options.discard(o.AST_DEPS)
            state.options.discard(o.AUTO_REFS)

        successors.processed = True

from .. import s_options as o

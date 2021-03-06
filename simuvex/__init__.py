#!/usr/bin/env python
"""
This module handles constraint generation.
"""

import logging
logging.getLogger("simuvex").addHandler(logging.NullHandler())
from .misc.loggers import Loggers
loggers = Loggers()
del Loggers
del logging

from .s_state import SimState
from .s_cc import SimCC, DefaultCC
from .s_slicer import SimSlicer
from .s_type import define_struct, register_types, parse_defns, parse_types, parse_file, parse_type

from . import storage
from . import concretization_strategies
from . import s_options
from . import s_type_backend

from .engines import SimEngine, SimSuccessors, SimEngineVEX
from .engines.vex.statements import SimIRStmt
from .engines.vex.irop import operations, all_operations, unsupported as unsupported_operations, unclassified as unclassified_operations

from .plugins import *
from .s_errors import *
from .s_action import *
from .s_pcap import PCAP
from .s_variable import *

options = s_options
o = s_options

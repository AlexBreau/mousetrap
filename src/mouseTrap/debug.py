# -*- coding: utf-8 -*-

# mouseTrap
#
# Copyright 2008 Flavio Percoco Premoli
#
# This file is part of mouseTrap.
#
# mouseTrap is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# mouseTrap is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with mouseTrap.  If not, see <http://www.gnu.org/licenses/>.

"""The debug module of mouseTrap."""

__id__        = "$Id$"
__version__   = "$Revision$"
__date__      = "$Date$"
__copyright__ = "Copyright (c) 2008 Flavio Percoco Premoli"
__license__   = "GPLv2"

import sys
import logging 
import traceback
import mouseTrap
import environment as env


modules = {}

def checkModule( module ):
    """
    Get's a new logger for modules.

    Arguments:
    - module: The module requesting a logger.
    """

    global modules

    level = logging.DEBUG

    try:
        if getattr( mouseTrap, "settings" ):
            level = mouseTrap.settings.getint("main", "debugLevel")
    except:
        level = logging.DEBUG
        
    formatter = logging.Formatter("%(levelname)s: %(name)s -> %(message)s")

    cli = logging.StreamHandler( )
    cli.setLevel( level )
    cli.setFormatter(formatter)

    file = logging.FileHandler( env.debugFile )
    file.setLevel( level )
    file.setFormatter(formatter)

    modules[module] = logging.getLogger( module )
    modules[module].addHandler(cli)
    modules[module].addHandler(file)
    modules[module].setLevel( level  )

def debug( module, message ):
    """
    Print DEBUG level log messages.

    Arguments:
    - module: The module sending the message
    - message: The message
    """

    if module not in modules:
        checkModule(module)

    modules[module].debug(message)


def info( module, message ):
    """
    Print INFO level log messages.

    Arguments:
    - module: The module sending the message
    - message: The message
    """

    if module not in modules:
        checkModule(module)

    modules[module].info(message)


def warning( module, message ):
    """
    Print WARNING level log messages.

    Arguments:
    - module: The module sending the message
    - message: The message
    """

    if module not in modules:
        checkModule(module)

    modules[module].warning(message)


def error( module, message ):
    """
    Print ERROR level log messages.

    Arguments:
    - module: The module sending the message
    - message: The message
    """

    if module not in modules:
        checkModule(module)

    modules[module].error(message)


def critical( module, message ):
    """
    Print CRITICAL level log messages.

    Arguments:
    - module: The module sending the message
    - message: The message
    """

    if module not in modules:
        checkModule(module)

    modules[module].critical(message)


def exception( module, message ):
    """
    Print EXCEPTION level log messages.

    Arguments:
    - module: The module sending the message
    - message: The message
    """

    if module not in modules:
        checkModule(module)

    modules[module].exception(message)

# The following code has been borrowed from the following URL:
# 
# http://www.dalkescientific.com/writings/diary/archive/ \
#                                     2005/04/20/tracing_python_code.html
#
import linecache

def traceit(frame, event, arg):
    """
    Line tracing utility to output all lines as they are executed by
    the interpreter.  This is to be used by sys.settrace and is for 
    debugging purposes.
   
    Arguments:
    - frame: is the current stack frame
    - event: 'call', 'line', 'return', 'exception', 'c_call', 'c_return',
             or 'c_exception'
    - arg:   depends on the event type (see docs for sys.settrace)
    
    Returns traceit
    """ 

    if event == "line":
        lineno = frame.f_lineno
        filename = frame.f_globals["__file__"]
        if (filename.endswith(".pyc") or
            filename.endswith(".pyo")):
            filename = filename[:-1]
        name = frame.f_globals["__name__"]
        if name == "gettext" \
           or name == "locale" \
           or name == "posixpath" \
           or name == "UserDict":
            return traceit
        line = linecache.getline(filename, lineno)
        log(ALL, "Trace", "TRACE %s:%s: %s" % (name, lineno, line.rstrip()))
    return traceit
    
#if debugLevel == EXTREME:
#    sys.settrace(traceit)

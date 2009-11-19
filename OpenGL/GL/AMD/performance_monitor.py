'''OpenGL extension AMD.performance_monitor

This module customises the behaviour of the 
OpenGL.raw.GL.AMD.performance_monitor to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.AMD.performance_monitor import *
### END AUTOGENERATED SECTION
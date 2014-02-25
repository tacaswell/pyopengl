'''OpenGL extension NV.multisample_coverage

This module customises the behaviour of the 
OpenGL.raw.GLX.NV.multisample_coverage to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/multisample_coverage.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper

import ctypes
from OpenGL.raw.GLX import _types
from OpenGL.raw.GLX.NV.multisample_coverage import *
from OpenGL.raw.GLX.NV.multisample_coverage import _EXTENSION_NAME

def glInitMultisampleCoverageNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION
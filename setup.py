import os
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


CYTHON_SOURCES = """src/p2t.pyx""".split("\n")
CPP_SOURCES = """poly2tri/common/shapes.cc
poly2tri/sweep/advancing_front.cc
poly2tri/sweep/cdt.cc
poly2tri/sweep/sweep.cc
poly2tri/sweep/sweep_context.cc""".split("\n")


mod_math = Extension(
    "p2t",
    CYTHON_SOURCES + CPP_SOURCES,
    language="c++"
)

setup(
    name="poly2tri",
    version="0.3.3",
    author="Mason Green",
    description="A 2D constrained Delaunay triangulation library",
    long_description=read('README'),
    url="http://code.google.com/p/poly2tri/",
    ext_modules=[mod_math],
    cmdclass={'build_ext': build_ext},
)

from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension("primes", sources=["prime_counter.pyx"]),
]
setup(
    ext_modules=cythonize([extensions[0]], annotate=True),
)

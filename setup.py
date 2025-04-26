from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

class BuildExt(build_ext):
    def build_extensions(self):
        for ext in self.extensions:
            ext.extra_compile_args = ['-std=c++11']
        super().build_extensions()

esl_module = Extension(
    name='ESL._ESL',
    sources=[
        'ESL/esl.c',
        'ESL/esl_buffer.c',
        'ESL/esl_config.c',
        'ESL/esl_event.c',
        'ESL/esl_json.c',
        'ESL/esl_threadmutex.c',
        'ESL/esl_oop.cpp',
        'ESL/ESL_wrap.cpp'
    ],
    include_dirs=['ESL'],
    extra_compile_args=['-std=c++11'],
    language='c++'
)

setup(
    name='python-ESL',
    version='1.4.18',
    description='FreeSWITCH Event Socket Library for Python',
    author='FreeSWITCH Developers',
    packages=['ESL'],
    ext_modules=[esl_module],
    cmdclass={'build_ext': BuildExt},
    zip_safe=False,
)


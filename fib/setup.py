from distutils.core import setup, Extension

py_ext = Extension("helloworld",
                    define_macros = [('MAJOR_VERSION','1'),
                                     ('MINOR_VERSION','0')],
                    #include_dirs = ['/usr/local/include'],
                    #libraries = ['tcl83'],
                    #library_dirs = ['/usr/local/lib'],
                    sources = ['hello.c'])

setup(name="Hello Package",
      version='1.0',
      ext_modules=[py_ext])

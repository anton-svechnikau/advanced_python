#include <Python.h>

static PyObject* helloworld(PyObject* self) {
  return Py_BuildValue("s", "Hello, Python extensions!");
}

static PyMethodDef helloworld_funcs[] = {
   {
       "helloworld",
       (PyCFunction)helloworld,
       METH_NOARGS,
       "Hello Python"
   },
   {NULL, NULL, 0, NULL}
};

#if PY_MAJOR_VERSION >= 3

static struct PyModuleDef moduledef = {
       PyModuleDef_HEAD_INIT,
       "helloworld",
       NULL,
       -1,
       helloworld_funcs
};

PyMODINIT_FUNC  PyInit_helloworld(void) {
  return PyModule_Create(&moduledef);
}

#else

PyMODINIT_FUNC inithelloworld(void) {
  Py_InitModule("helloworld",  helloworld_funcs);
}

#endif

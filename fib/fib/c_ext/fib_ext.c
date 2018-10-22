#include <Python.h>
#include <stdio.h>

static PyObject* fib(PyObject* self, PyObject* args) {
    const unsigned int iterations;
    unsigned long long first = 0;
    unsigned long long second = 1;
    unsigned long long next;
    unsigned int i;

    if (!PyArg_ParseTuple(args, "i", &iterations)) {
        return NULL;
    }

    for (i = 0; i < iterations; i++) {
        if (i <= 1) {
            next = i;
        } else {
            next = first + second;
            first = second;
            second = next;
        }
        printf("%Lu\n", next);
    }

    Py_RETURN_NONE;
}

static PyMethodDef fib_funcs[] = {
   {
       "fib",
       (PyCFunction)fib,
       METH_VARARGS,
       "Fibonacci"
   },
   {NULL, NULL, 0, NULL}
};

#if PY_MAJOR_VERSION >= 3

static struct PyModuleDef moduledef = {
       PyModuleDef_HEAD_INIT,
       "fib_c",
       NULL,
       -1,
       fib_funcs
};

PyMODINIT_FUNC  PyInit_fib(void) {
    return PyModule_Create(&moduledef);
}

#else

PyMODINIT_FUNC initfib(void) {
    Py_InitModule("fib_c", fib_funcs);
}

#endif

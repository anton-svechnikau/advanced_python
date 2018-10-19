#include <Python.h>
#include <stdio.h>

static PyObject* fib(PyObject* self, PyObject* args) {
    const int* iterations;
    int first = 0;
    int second = 1;
    int next;

    if (!PyArg_ParseTuple(args, "d", &iterations)) {
        return NULL;
    }

    for (int i = 0; i < iterations; i++) {
        if (i <= 0) {
            next = i;
        } else {
            next = first + second;
            first = second;
            second = next;
        }
        printf("%d\n", next);
    }

  return Py_BuildValue("s", "Hello, Python extensions!");
}

static PyMethodDef helloworld_funcs[] = {
   {
       "fib",
       (PyCFunction)fib,
       METH_NOARGS,
       "Fibonacci"
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





int fib(int n) {
    int first = 0;
    int second = 1;
    int next;

    for (int x = 0; x < n; x++) {
        if (x <= 1) {
            next = x;
        } else {
            next = first + second;
            first = second;
            second = next;
        }
        printf("%d\n", next);
    }
    return 0;
}

int main(void) {
    fib(5);
    return 0;
}



#include "python.h"
#include <stdlib.h>

/**
 * print_python_list_info - function that prints some basic
 * info about Python lists.
 * @p: pointer to generic PyObkect
 * Return: Nothing
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *list = NULL;
	size_t length = 0, i = 0;
	const char *p_type = NULL;

	length = PyList_size(p);
	list = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", length);
	printf("[*] Allocated = %ld\n", (signed long)(list->allocated));
	for (i = 0; i < length; i++)
	{
		p_type = Py_TYPE(list->ob_item[i])->tp_name;
		printf("Element %ld: %s\n", i, p_type);
	}
}

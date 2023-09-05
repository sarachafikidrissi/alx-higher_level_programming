#include "lists.h"
/**
 * check_cycle - a function that checks if a single list
 * has a cycle or not
 * @list: a pointer to the adress of first node
 * Return: 1 if cycle exist otherwise 0
 */
int check_cycle(listint_t *list)
{
	listint_t *temp1, *temp2;

	if (list == NULL)
		return (0);

	temp1 = list;
	temp2 = list->next;

	while (temp1 && temp2)
	{
		if (temp2->next == NULL)
			return (0);
		temp1 = temp1->next;
		temp2 = temp2->next->next;

		if (temp1 == temp2)
			return (1);
	}
	free(temp1);
	free(temp2);

	return (0);
}

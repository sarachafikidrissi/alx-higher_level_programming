#include "lists.h"
/**
 *
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
		if (temp2 ->next == NULL)
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

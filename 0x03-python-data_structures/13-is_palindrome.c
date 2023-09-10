#include "lists.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - a function that checks if a singly lilnked
 * list is a palindrome
 * @head: a double pointer that holds the adress of the node pointer
 * Return: 1 if list is palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int count = 0, i = 0, *array = NULL;

	if (*head == NULL || head == NULL || (*head)->next == NULL)
		return (1);
	while (temp)
	{
		count++;
		temp = temp->next;
	}
	array = malloc(sizeof(int) * count);
	temp = *head;
	while (temp)
	{
		array[i++] = temp->n;
		temp = temp->next;
	}
	for (i = 0; i < count / 2; i++)
	{
		if (array[i] != array[count - 1 -i])
		{
			free(array);
			return(0);
		}
	}
	free(array);
	return (1);
}

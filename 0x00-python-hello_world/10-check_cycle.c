#include "lists.h"

/**
 * check_cycle - checks for cycle in the list
 * @list: the list to check
 *
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;

	temp = list;
	while (temp->next == 0)
	{
		temp = temp->next;
		if (temp->next == list)
		{
			return (1);
		}
	}
	return (0);
}

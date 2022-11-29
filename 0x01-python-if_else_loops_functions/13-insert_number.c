#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *prev,  *newnode;
	
	current = *head;
	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (0);

	while (current != NULL)
	{
		if (current->n >= number)
			break;
		prev = current;
		current = current->next;
	}
	
	newnode->n = number;
	
	if (*head == NULL)
	{
		*head = newnode;
		newnode->next = NULL;
	}
	else
	{
		newnode->next = current;
		prev->next = newnode;
	}

	return (newnode);
}

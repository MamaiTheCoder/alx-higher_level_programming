#include "lists.h"

/**
 * reverse_list - reverse the list
 * @head_two: head to list
 *
 * Return: Void.
 */
void reverse_list(listint_t **head)
{
	listint_t *prev_node, *curr_node, *next_node;

	prev_node = 0;
	curr_node = next_node = *head;
	
	while (curr_node != NULL)
	{
		next_node = next_node->next;
		curr_node->next = prev_node;
		prev_node = curr_node;
		curr_node = next_node;
	}
	*head = prev_node;
}

int compare(listint_t *h1, listint_t *h2)
{
	listint_t *temp1, *temp2;

	temp1 = h1;
	temp2 = h2;

	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
		{
			return (0);
		}
	}

	if (temp1 == NULL && temp2 == NULL)
		return (1);

	return (0);
}
/**
 * is_palindrome - checks if its a palindrome
 *
 * @head: head to the list
 *
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow;
	listint_t *scn_half, *middle;
	int isp;

	slow = fast = prev_slow = *head;
	middle = NULL;
	isp = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			middle = slow;
			slow = slow->next;
		}

		scn_half = slow;
		prev_slow->next = NULL;
		reverse_list(&scn_half);
		isp = compare(*head, scn_half);

		if (middle != NULL)
		{
			prev_slow->next = middle;
			middle->next = scn_half;
		}
		else
		{
			prev_slow->next = scn_half;
		}
	}

	return (isp);
}

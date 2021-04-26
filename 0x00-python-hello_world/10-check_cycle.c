#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in a linked list
 * @list: list to be checked
 *
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *first = NULL;
	listint_t *second = NULL;

	if (list == NULL)
		return (0);
	first = list;
	second = first->next;
	if (second == NULL)
		return (0);
	second = second->next;
	while (first != NULL && second != NULL)
	{
		if (first == second)
			return (1);
		first = first->next;
		if (second->next == NULL)
			break;
		second = (second->next)->next;
	}
	return (0);
}

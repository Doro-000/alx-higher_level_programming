#include "lists.h"

/**
 * insert_node - inserts a node in a sorted linked list
 * @head: head of list to be used
 * @number: content of the node
 *
 * Return: address of the node inserted, NULL otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev = NULL;
	listint_t *current = NULL;
	listint_t *new = NULL;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	current = *head;
	while (current != NULL)
	{
		if (current->n >= number && prev == NULL)
		{
			*head = new;
			new->next = current;
			return (new);
		}
		else if (current->n >= number)
		{
			prev->next = new;
			new->next = current;
			return (new);
		}
		prev = current;
		current = current->next;
	}
	prev->next = new;
	return (new);
}

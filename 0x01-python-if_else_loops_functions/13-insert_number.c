#include "lists.h"

/**
 * insert_node - inserts a node in a sorted linked list
 * @head: head of list to be used
 *
 * Return: address of the node inserted, NULL otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev = NULL;
	listint_t *after = NULL;
	listint_t *new = NULL;
	listint_t *current = NULL;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	current = *head;
	if (current == NULL)
	{
		prev = new;
		return (new);
	}
	while (current != NULL)
	{
		
		if (current->n >= number)
		{
			prev->next = new;
			new->next = current;
		}
	}
}

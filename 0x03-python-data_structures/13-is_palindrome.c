#include "lists.h"

int list_len(listint_t *);

/**
 * list_len - counts the number of nodes in a linked list
 * @h: head of the list
 *
 * Return: the number of elements
 */
int list_len(listint_t *h)
{
	listint_t *cursor = h;
	int count = 0;

	while (cursor != NULL)
	{
		count += 1;
		cursor = cursor->next;
	}
	return (count);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: head of the list
 *
 * Return: 1 if it's a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *cursor = NULL;
	int *elements = NULL;
	int size, i;

	if (head == NULL)
		return (0);
	cursor = *head;
	if (cursor == NULL)
		return (1);
	size = list_len(cursor);
	elements = malloc(sizeof(*elements) * size);
	if (elements == NULL)
		return (0);
	for (i = 0; i < size; i++)
	{
		elements[i] = cursor->n;
		cursor = cursor->next;
	}
	for (i = 0; i < size; i++, size--)
	{
		if (elements[i] != elements[size - 1])
		{
			free(elements);
			return (0);
		}
	}
	free(elements);
	return (1);
}

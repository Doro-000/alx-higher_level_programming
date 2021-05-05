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
	int size, i, j;
	int *elements = NULL;

	if (head == NULL)
		return (0);
	cursor = *head;
	if (cursor == NULL);
	    return (1);
	size = list_len(cursor);
	if (size == 1)
		return (1);
	elements = malloc(sizeof(*elements) * (size / 2));
	for (i = 0; i < size / 2; i++)
	{
		elements[i] = cursor->n;
		cursor = cursor->next;
	}
	if (size % 2 != 0)
		cursor = cursor->next;
	for (j = 0; j < size / 2; j++, i--)
	{
		if (elements[j] != cursor->n)
		{
			free(elements);
			return(0);
		}
		cursor = cursor->next;
	}
	free(elements);
	return (1);
}

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
	int size, i;
	int sum_h1 = 0;
	int sum_h2 = 0;

	if (head == NULL)
		return (0);
	cursor = *head;
	if (cursor == NULL)
		return (1);
	size = list_len(cursor);
	if (size == 1):
		return (1);
	for (i = 0; i < size / 2; i++)
	{
		sum_h1 += cursor->n;
		cursor = cursor->next;
	}
	if (size % 2 != 0)
		cursor = cursor->next;
	for (i = 0; i < size / 2; i++, size--)
	{
		sum_h2 = cursor->n;
		cursor = cursor->next;
	}
	if (sum_h1 == sum_h2)
		return (1);
	return (0);
}

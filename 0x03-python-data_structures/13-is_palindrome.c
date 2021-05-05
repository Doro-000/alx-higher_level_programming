#include "lists.h"

int list_len(listint_t *);
listint_t *reverse_listint(listint_t **);

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
 * reverse_listint - reverses a linked list
 * @head: head of the list
 *
 * Return: the first node of the reversed node
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *next_node = NULL;
	listint_t *prev_node = NULL;

	if (head == NULL)
		return (NULL);
	while (*head != NULL)
	{
		next_node = (*head)->next;
		(*head)->next = prev_node;
		prev_node = *head;
		*head = next_node;
	}
	*head = prev_node;
	return (*head);
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
	listint_t *cursor_2 = NULL;
	int size, i;

	if (head == NULL)
		return (0);
	cursor = *head;
	cursor_2 = *head;
	if (cursor == NULL)
		return (1);
	size = list_len(*head);
	for (i = 0; i < size / 2; i++)
		cursor = cursor->next;
	if (size % 2 != 0)
		cursor = cursor->next;
	cursor = reverse_listint(&cursor);
	for (i = 0; i < size / 2; i++)
	{
		if (cursor_2->n != cursor->n)
			return (0);
		cursor_2 = cursor_2->next;
		cursor = cursor->next;
	}
	return (1);
}

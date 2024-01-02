#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *slug, *rocket;

	if (list == NULL || list->next == NULL)
		return (0);

	slug = list->next;
	rocket = list->next->next;

	while (slug && rocket && rocket->next)
	{
		if (slug == rocket)
			return (1);

		slug = slug->next;
		rocket = rocket->next->next;
	}

	return (0);
}

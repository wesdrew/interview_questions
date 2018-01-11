/* Linked List implementation, with help from Mastering Algorithms with C by Kyle Loudon*/


#ifndef LIST_H
#define LIST_H

#include "node.h"

typedef struct _list{
  unsigned int size;
  Node *head;
  Node *tail;

  void (*destroy)(void *data); 	/* destroy function for stored data type */
  int (*match)(void *item_1, void *item_2); /* compare function for stored data type */
} List;


/* initialization */
int list_init(List *list, void (*destroy)(void *data), 
	      int (*match)(void *item_1, void *item_2));

/* getter methods */
Node *get_list_head(List *list);
Node *get_list_tail(List *list);
//Node *get_kth_node(List *list, int k);

/* setter methods */ 
void _set_list_head(List *list, Node *n);
void _set_list_tail(List *list, Node *n);

/* list destruction */
void destroy_list(List *list);

/* state methods */
int is_empty(List *list);
int _get_size(List *list);

#endif

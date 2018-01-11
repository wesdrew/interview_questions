#ifndef NODE_H
#define NODE_H

#include <stdlib.h>

typedef struct _node {
  void *data;
  struct _node *next;
  struct _node *prev;
} Node;


Node *get_next_node(Node *n);
Node *get_prev_node(Node *n);
void *get_node_data(Node *n);
void set_node_data(Node *n, void *data);
int _has_next(Node *n);
int _has_prev(Node *n);
void _set_next_node(Node *n, Node *next);
void _set_prev_node(Node *n, Node *prev);
void _unlink_node(Node *n); 	/* set node's pointers to null */

#endif

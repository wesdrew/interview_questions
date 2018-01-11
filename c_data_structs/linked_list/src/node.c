#include "../include/node.h"

Node *get_next_node(Node *n) {
  return n->next;
}

Node *get_prev_node(Node *n) {
  return n->prev;
}

void *get_node_data(Node *n) {
  return n->data;
}

void set_node_data(Node *n, void *data) {
  n->data = data;
}

int _has_next(Node *n) {
  return n->next != NULL ? 1 : 0;
}

int _has_prev(Node *n) {
  return n->prev != NULL ? 1 : 0;
}

void _set_next_node(Node *n, Node *next) {
  n->next = next;
}

void _set_prev_node(Node *n, Node *prev) {
  n->prev = prev;
}

void _unlink_node(Node *n) {	/* set this node's pointers to null */
  _set_next_node(n, NULL);
  _set_prev_node(n, NULL);
}
  

#include "../include/list.h"
#include <stdio.h>

int list_init(List *list, void (*destroy)(void *data),
	      int (*match)(void *item_1, void *item_2)) {
  Node *n = malloc(sizeof(Node));
  if (n != NULL) {
    list->size = 0;
    list->head = n;
    list->tail = n;
    n = NULL;
    list->destroy = destroy;
    list->match = match;
    return 1; 
  }
  return 0;
}

/* getter methods */
Node *get_list_head(List *list) {
  return list->head;
}

Node *get_list_tail(List *list) {
  return list->tail;
}

/* setter methods */

void _set_list_head(List *list, Node *n) {
  list->head = n;
}

void _set_list_tail(List *list, Node *n) {
  list->tail = n;
}

/* list destruction */
void destroy_list(List *list){
  Node *next, *to_delete;
  while (!is_empty(list)) {
    to_delete = get_list_head(list);
    _set_list_head(list, get_next_node(to_delete));
    // list->destroy(get_node_data(to_delete)); // not sure how to implement destroy!
    _unlink_node(to_delete);
    free(to_delete);
    list->size--;
  }
}

/* state methods */
int is_empty(List *list) {
  return _get_size(list) == 0 ? 1 : 0;
}

int _get_size(List *list) { 
  return list->size;
}

/* append! note - we should do type checking in future  */
int append(List *list, void *data) {
  Node *n = malloc(sizeof(Node));
  void *saved = malloc(sizeof(void *));
  if (n != NULL && saved != NULL) {
    saved = data;
    set_node_data(n, saved);
    _unlink_node(n);		/* just a precaution */
    _append(list, n);
    list->size++;
    return 1;
  }
  else {
    return 0;
  }
}

void _append(List *list, Node *node) {
  if (is_empty(list)) {
    _set_list_head(list, node);
    _set_list_tail(list, node);
  }
  else {
    _set_prev_node(node, get_list_tail(list));
    _set_next_node(get_list_tail(list), node);
    _set_list_tail(list, node);
  }
}

/* removing data */

int pop(List *list, void **data) {
  Node *n;
  if (_pop(list, &n)) {
    *data = get_node_data(n);
    //list->destroy(get_node_data(n));
    free(n);
    return 1;
  }
  return 0;
}

int dequeue(List *list, void **data) {
  Node *n;
  if (_dequeue(list, &n)) {
    *data = get_node_data(n);
    free(n);
    //list->destroy(get_node_data(n));
    return 1;
  }
  return 0;
}


int _pop(List *list, Node **n) {
  if (!is_empty(list)) {
    *n = get_list_tail(list);
    _set_list_tail(list, get_prev_node(*n));
    _unlink_node(*n);
    list->size--;
    return 1;
  }
  return 0;
}

int _dequeue(List *list, Node **n) {
  if (!is_empty(list)) {
    *n = get_list_head(list);
    _set_list_head(list, get_next_node(*n));
    _unlink_node(*n);
    list->size--;
    return 1;
  }
  return 0;
}

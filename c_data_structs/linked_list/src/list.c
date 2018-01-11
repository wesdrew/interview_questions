#include "../include/list.h"


int list_init(List *list, void (*destroy)(void *data),
	      int (*match)(void *item_1, void *item_2)) {
  Node *n;
  list = malloc(sizeof(List));
  n = malloc(sizeof(Node));
  if (n != NULL && list != NULL) {
    list->size = 0;
    list->head = n;
    list->tail = n;
    list->destroy = destroy;
    list->match   = match;
    return 1; 			/* good to go! */
  }
  return 0;			/* a malloc failed! */
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
  _set_next_node(n, list->head);
  _set_prev_node(n, NULL);
  list->head = n;
}

void _set_list_tail(List *list, Node *n) {
  _set_prev_node(n, list->tail);
  _set_next_node(n, NULL);
  list->tail = n;
}

/* list destruction */
void destroy_list(List *list){
  Node *next, *to_delete;
  while (!is_empty(list)) {
    to_delete = get_list_head(list);
    _set_list_head(list, get_next_node(to_delete));
    list->destroy(get_node_data(to_delete));
    _unlink_node(to_delete);
    free(to_delete);
  }
  free(list);
}

/* state methods */
int is_empty(List *list) {
  return _get_size(list) > 0 ? 1 : 0;
}

int _get_size(List *list) { 
  return list->size;
}

/* append! note - we should do type checking in future  */
int append(List *list, void *data) {
  Node *n = malloc(sizeof(Node));
  if (n != NULL) {
    set_node_data(n, data);
    _set_prev_node(n, get_list_tail(list));
    _set_next_node(n, NULL);
    _set_next_node(get_list_tail(list), n);
    list->size++;
    return 1;
  }
  else {
    return 0;
  }
}

/* removing data - helper methods */

int _pop(List *list, Node *n) {
  if (!is_empty(list)) {
    n = get_list_tail(list);
    _set_list_tail(list, get_prev_node(n));
    _unlink_node(n);
    list->size--;
    return 1;
  }
  else {
    return 0;
  }
}

int _dequeue(List *list, Node *n) {
  if (!is_empty(list)) {
    n = get_list_head(list);
    _set_list_head(list, get_next_node(n));
    _unlink_node(n);
    list->size--;
    return 1;
  }
  else {
    return 0;
  }
}

/* removing data */

int pop(List *list, void *data) {
  Node *n;
  if (_pop(list, n)) {
    memcpy(get_node_data(n), data, sizeof(void *)); /* save data */
    list->destroy(get_node_data(n)); /* free malloc-ed space */
    free(n);
    return 1;
  }
  else {
    return 0;
  }
}

int dequeue(List *list, void *data) {
  Node *n;
  if (_dequeue(list, n)) {
    memcpy(get_node_data(n), data, sizeof(void *));
    list->destroy(get_node_data(n));
    free(n);
    return 1;
  }
  else {
    return 0;
  }
}

#include "../include/node.h"
#include <stdio.h>
#include <assert.h>

int main(int argc, char **argv) {

  Node n, prev, next;
  set_node_data(&n, (void *) &("test\0"));
  set_node_data(&prev, (void *) &("this is the prev node's data\0"));
  set_node_data(&next, (void *) &("this is the next node's data\0"));
  _set_prev_node(&n, &prev);
  _set_next_node(&n, &next);
  assert(_has_prev(&n));
  assert(_has_next(&n));
  printf("%s\n", get_node_data(&n));
  printf("%s\n", get_node_data(&prev));
  printf("%s\n", get_node_data(&next));
  _unlink_node(&n);
  assert(!_has_prev(&n));
  assert(!_has_next(&n));
}

#include "../include/list.h"
#include <assert.h>
#include <stdio.h>

int main(int argc, char **argv) {
  List test;
  list_init(&test, &free, NULL);
  assert(is_empty(&test));
  char *test_strings[] = {"the\0", "land\0", "of\0", "chocolate\0"};
  for (int i = 0; i < 4; i++) {
    append(&test, (void *) test_strings[i]);
  }
  void *to_print;
  /*  for (int j = 0; j < 4; j++) {
    pop(&test, to_print);
    printf("%s\n", (char *) to_print); 
    }*/
  printf("%s\n", test.head->data);
  printf("%s\n", test.head->next->data);
  printf("%s\n", test.head->next->next->data);
}

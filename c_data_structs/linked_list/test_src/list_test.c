#include "../include/list.h"
#include <assert.h>
#include <stdio.h>



void test_set_list_head(List *list) {
  printf("testing set_list_head\n");
  printf("\tprinting address of list head\n");
  while ((get_list_head(list))) {
    printf("\tlist head == %p\n", get_list_head(list));
    _set_list_head(list, get_next_node(get_list_head(list)));
  }
}


void test_set_list_tail(List *list) {
  printf("testing set_list_tail\n");
  printf("\tprinting address of list tail\n");
  while ((get_list_tail(list))) {
    printf("\tlist tail == %p\n", get_list_tail(list));
    _set_list_tail(list, get_prev_node(get_list_tail(list)));
  }
}

void reset_head_tail_pointers(List *list, Node *head, Node *tail) {
  _set_list_tail(list, tail);
  _set_list_head(list, head);
}


void append_to_linked_list(List *list, char **strings, int count) {
  for (int i = 0; i < count; i++) {
    append(list, strings[i]);
  }
}


void test_list_pointers(List *list) {
  Node *saved_head = list->head;
  Node *saved_tail  = list->tail;

  /* testing set_list_head */
  
  test_set_list_head(list);
  printf("saved list head: %p\n", saved_head);
  printf("current list head: %p\n", list->head);  

  /* testing set_list_tail */
  test_set_list_tail(list);
  printf("saved list tail: %p\n", saved_tail);
  printf("current list tail: %p\n", list->tail);
  reset_head_tail_pointers(list, saved_head, saved_tail);
  printf("reset pointers! head @ %p, tail @ %p\n", get_list_head(list), get_list_tail(list));

}

void test_pop(List *list) {
  char *to_print;
  printf("\t testing pop...\n");
  for (int i = 0; i < 4; i++) {
    pop(list, (void **) &to_print);
    printf("\t\t%s\n", to_print);
  }
}

void test_dequeue(List *list) {
  char *to_print;
  printf("\t testing dequeue...\n");
  for (int i = 0; i < 4; i++) {
    dequeue(list, (void **) &to_print);
    printf("\t\t%s\n", to_print);
  }
}



void announce_test_strings(char **strings) {
  printf("\t our test strings are...\n");
  for (int i = 0; i < 4; i++) {
    printf("\t\t%s\n", strings[i]);
  }


}  

void test_list_delete(List *list) {
  destroy_list(list);
  assert(is_empty(list));
}


int main(int argc, char **argv) {
  List test_list;
  list_init(&test_list, &free, NULL);
  assert(is_empty(&test_list));
  char *test_strings[] = {"the\0", "land\0", "of\0", "chocolate\0"};
  append_to_linked_list(&test_list, test_strings, 4);
  test_list_pointers(&test_list);
  printf("testing pop, dequeue\n");
  announce_test_strings(test_strings);
  test_pop(&test_list);
  printf("\treloading list!\n");
  append_to_linked_list(&test_list, test_strings, 4);
  test_dequeue(&test_list);
  append_to_linked_list(&test_list, test_strings, 4);
  test_list_delete(&test_list);  
}

CC = gcc

list_test: list_test.o list.o
	$(CC) -o list_test list_test.o list.o


list_test.o: list.h
	$(CC) -c list_test.c -o list_test.o

list.o: list.c list.h
	$(CC) -c list.c -o list.o

clean:
	rm list_test $(OBJECTS)
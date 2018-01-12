CC = gcc
INCLUDE=./include
SRC=./src
BIN=./bin
TEST_SRC=./test_src
TEST_BIN=./test_bin
EXEC=./exec
ALL_DIRS= $(SRC) $(TEST_SRC) $(BIN) $(TEST_BIN) $(EXEC) $(INCLUDE)
BIN_DIRS= $(BIN) $(TEST_BIN)
SRC_DIRS= $(SRC) $(TEST_SRC)

test: list_test node_test

list_test: list_test.o list.o node.o
	$(CC) -o $(EXEC)/list_test $(TEST_BIN)/list_test.o $(BIN)/list.o $(BIN)/node.o

node_test: node_test.o node.o
	$(CC) -o $(EXEC)/node_test $(TEST_BIN)/node_test.o $(BIN)/node.o

node_test.o:
	$(CC) -c $(TEST_SRC)/node_test.c -o $(TEST_BIN)/node_test.o

list_test.o:
	$(CC) -c $(TEST_SRC)/list_test.c -o $(TEST_BIN)/list_test.o

list.o: $(SRC)/list.c $(INCLUDE)/list.h
	$(CC) -c $(SRC)/list.c -o $(BIN)/list.o

node.o: $(SRC)/node.c $(INCLUDE)/node.h
	$(CC) -c $(SRC)/node.c -o $(BIN)/node.o

.PHONY: clean mkdir

clean:
	for dir in $(BIN_DIRS) ; do \
		rm $$dir/* ; \
	done
	rm $(EXEC)/*

mkdir:
	for dir in $(ALL_DIRS) ; do \
		mkdir $$dir ; \
	done

CC = gcc
FLAGS = -Wall
OUT = list

all: main

main: main.c list error
	$(CC) $(FLAGS) main.c list.o error.o -o $(OUT)

list: list.c
	$(CC) $(FLAGS) -c list.c

error: error.c
	$(CC) $(FLAGS) -c error.c

clean:
	rm -rf *.o $(OUT)

CC = gcc
FLAGS = -Wall -O3
OBJS = list.o error.o

SOURCEDIR = "src/"
OUT = "bin/list"
OBJS = $(shell find . -name '*.o')

SRC = $(pathsubst %.c)
.PHONY: clean

all: objs
	$(CC) $(OBJS) -o $(OUT)

objs:
	$(CC) -c $(OBJS)

clean:
	rm -rf *.o $(OUT)

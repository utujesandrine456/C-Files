#ifndef AUTHOR_H
#define AUTHOR_H

typedef struct {
    int author_id;
    char name[100];
    char bio[500];
} Author;

void addAuthor();
void viewAuthors();

#endif

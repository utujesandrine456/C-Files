#ifndef BOOK_H
#define BOOK_H

typedef struct {
    int book_id;
    char title[100];
    int author_id;
    int publisher_id;
    char isbn[20];
    char genre[50];
    int year_published;
    int copies_available;
    char shelf_location[30];
} Book;

void addBook();
void viewBooks();

#endif

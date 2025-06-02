#ifndef BORROW_H
#define BORROW_H

#include <stdbool.h>

typedef struct {
    int borrowing_id;
    int book_id;
    int member_id;
    char borrow_date[20];
    char due_date[20];
    char return_date[20]; // Can be empty string if not returned
    int staff_id;
} Borrowing;

void addBorrowing();
void viewBorrowings();

#endif
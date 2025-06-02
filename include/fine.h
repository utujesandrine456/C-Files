#ifndef FINE_H
#define FINE_H

#include <stdbool.h>

typedef struct {
    int fine_id;
    int borrowing_id;
    double amount;
    bool paid;
    char date_paid[20]; // empty if not paid
} Fine;

void addFine();
void viewFines();

#endif

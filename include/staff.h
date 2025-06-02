#ifndef STAFF_H
#define STAFF_H

typedef struct {
    int staff_id;
    char name[100];
    char role[50];
    char email[100];
    char phone[20];
} Staff;

void addStaff();
void viewStaff();

#endif
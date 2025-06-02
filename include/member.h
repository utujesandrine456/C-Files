#ifndef MEMBER_H
#define MEMBER_H

typedef struct {
    int member_id;
    char name[100];
    char address[200];
    char phone[20];
    char email[100];
    char date_joined[20];
    char membership_status[20];
} Member;

void addMember();
void viewMembers();

#endif
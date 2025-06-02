#ifndef PUBLISHER_H
#define PUBLISHER_H

typedef struct {
    int publisher_id;
    char name[100];
    char address[200];
    char contact_info[100];
} Publisher;

void addPublisher();
void viewPublishers();

#endif
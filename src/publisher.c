#include <stdio.h>
#include <string.h>
#include "../include/publisher.h"

void addPublisher() {
    FILE *fp = fopen("../data/publishers.dat", "ab");
    if (!fp) {
        printf("Error: Cannot open publishers file!\n");
        return;
    }

    Publisher p;
    printf("\n=== Add New Publisher ===\n");
    printf("Enter Publisher ID: "); scanf("%d", &p.publisher_id);
    while (getchar() != '\n'); // Clear input buffer
    printf("Name: "); fgets(p.name, 100, stdin); strtok(p.name, "\n");
    printf("Address: "); fgets(p.address, 200, stdin); strtok(p.address, "\n");
    printf("Contact Info: "); fgets(p.contact_info, 100, stdin); strtok(p.contact_info, "\n");

    fwrite(&p, sizeof(Publisher), 1, fp);
    fclose(fp);
    printf("Publisher added successfully!\n");
}

void viewPublishers() {
    FILE *fp = fopen("../data/publishers.dat", "rb");
    if (!fp) {
        printf("Error: No publishers found!\n");
        return;
    }

    Publisher p;
    printf("\n=== Publisher List ===\n");
    while (fread(&p, sizeof(Publisher), 1, fp)) {
        printf("ID: %d | Name: %s | Address: %s | Contact: %s\n",
               p.publisher_id, p.name, p.address, p.contact_info);
    }

    fclose(fp);
}
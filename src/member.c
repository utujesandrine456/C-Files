#include <stdio.h>
#include <string.h>
#include "../include/member.h"

void addMember() {
    FILE *fp = fopen("../data/members.dat", "ab");
    if (!fp) {
        printf("Error: Cannot open members file!\n");
        return;
    }

    Member m;
    printf("\n=== Add New Member ===\n");
    printf("Enter Member ID: "); scanf("%d", &m.member_id);
    while (getchar() != '\n'); // Clear input buffer
    printf("Name: "); fgets(m.name, 100, stdin); strtok(m.name, "\n");
    printf("Address: "); fgets(m.address, 200, stdin); strtok(m.address, "\n");
    printf("Phone: "); fgets(m.phone, 20, stdin); strtok(m.phone, "\n");
    printf("Email: "); fgets(m.email, 100, stdin); strtok(m.email, "\n");
    printf("Date Joined (YYYY-MM-DD): "); fgets(m.date_joined, 20, stdin); strtok(m.date_joined, "\n");
    printf("Membership Status: "); fgets(m.membership_status, 20, stdin); strtok(m.membership_status, "\n");

    fwrite(&m, sizeof(Member), 1, fp);
    fclose(fp);
    printf("Member added successfully!\n");
}

void viewMembers() {
    FILE *fp = fopen("../data/members.dat", "rb");
    if (!fp) {
        printf("Error: No members found!\n");
        return;
    }

    Member m;
    printf("\n=== Member List ===\n");
    while (fread(&m, sizeof(Member), 1, fp)) {
        printf("ID: %d | Name: %s | Address: %s | Phone: %s | Email: %s | Joined: %s | Status: %s\n",
               m.member_id, m.name, m.address, m.phone, m.email, m.date_joined, m.membership_status);
    }

    fclose(fp);
}
#include <stdio.h>
#include <string.h>
#include "../include/staff.h"

#define FILE_PATH "../data/staffs.dat"

void addStaff() {
    FILE *fp = fopen(FILE_PATH, "ab");
    if (!fp) {
        printf("Error: Cannot open staff file!\n");
        return;
    }

    Staff s;
    printf("\n=== Add New Staff ===\n");
    printf("Enter Staff ID: "); scanf("%d", &s.staff_id);
    while (getchar() != '\n'); // Clear input buffer
    printf("Name: "); fgets(s.name, 100, stdin); strtok(s.name, "\n");
    printf("Role: "); fgets(s.role, 50, stdin); strtok(s.role, "\n");
    printf("Email: "); fgets(s.email, 100, stdin); strtok(s.email, "\n");
    printf("Phone: "); fgets(s.phone, 20, stdin); strtok(s.phone, "\n");

    fwrite(&s, sizeof(Staff), 1, fp);
    fclose(fp);
    printf("Staff added successfully!\n");
}

void viewStaff() {
    FILE *fp = fopen(FILE_PATH, "rb");
    if (!fp) {
        printf("Error: No staff found!\n");
        return;
    }

    Staff s;
    printf("\n=== Staff List ===\n");
    while (fread(&s, sizeof(Staff), 1, fp)) {
        printf("ID: %d | Name: %s | Role: %s | Email: %s | Phone: %s\n",
               s.staff_id, s.name, s.role, s.email, s.phone);
    }

    fclose(fp);
}
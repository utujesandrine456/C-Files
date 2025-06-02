#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include "../include/fine.h"

void addFine() {
    FILE *fp = fopen("../data/fines.dat", "ab");
    if (!fp) {
        printf("Error: Cannot open fines file!\n");
        return;
    }

    Fine f;
    printf("\n=== Add New Fine ===\n");
    printf("Enter Fine ID: "); scanf("%d", &f.fine_id);
    printf("Borrowing ID: "); scanf("%d", &f.borrowing_id);
    printf("Amount: "); scanf("%lf", &f.amount);
    printf("Paid (1 for yes, 0 for no): "); int paid; scanf("%d", &paid);
    f.paid = paid ? true : false;
    while (getchar() != '\n'); // Clear input buffer
    if (f.paid) {
        printf("Date Paid (YYYY-MM-DD): "); fgets(f.date_paid, 20, stdin); strtok(f.date_paid, "\n");
    } else {
        f.date_paid[0] = '\0';
        printf("Fine marked as unpaid.\n");
    }

    fwrite(&f, sizeof(Fine), 1, fp);
    fclose(fp);
    printf("Fine added successfully!\n");
}

void viewFines() {
    FILE *fp = fopen("../data/fines.dat", "rb");
    if (!fp) {
        printf("Error: No fines found!\n");
        return;
    }

    Fine f;
    printf("\n=== Fine List ===\n");
    while (fread(&f, sizeof(Fine), 1, fp)) {
        printf("Fine ID: %d | Borrowing ID: %d | Amount: %.2f | Paid: %s | Date Paid: %s\n",
               f.fine_id, f.borrowing_id, f.amount, f.paid ? "Yes" : "No", f.date_paid);
    }

    fclose(fp);
}
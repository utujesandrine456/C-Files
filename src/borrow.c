#include <stdio.h>
#include <string.h>
#include "../include/borrow.h"

void addBorrowing() {
    FILE *fp = fopen("../data/borrowings.dat", "ab");
    if (!fp) {
        printf("Error: Cannot open borrowings file!\n");
        return;
    }

    Borrowing b;
    printf("\n=== Add New Borrowing ===\n");
    printf("Enter Borrowing ID: "); scanf("%d", &b.borrowing_id);
    printf("Book ID: "); scanf("%d", &b.book_id);
    printf("Member ID: "); scanf("%d", &b.member_id);
    while (getchar() != '\n'); // Clear input buffer
    printf("Borrow Date (YYYY-MM-DD): "); fgets(b.borrow_date, 20, stdin); strtok(b.borrow_date, "\n");
    printf("Due Date (YYYY-MM-DD): "); fgets(b.due_date, 20, stdin); strtok(b.due_date, "\n");
    printf("Return Date (YYYY-MM-DD or empty): "); fgets(b.return_date, 20, stdin); strtok(b.return_date, "\n");
    printf("Staff ID: "); scanf("%d", &b.staff_id);

    fwrite(&b, sizeof(Borrowing), 1, fp);
    fclose(fp);
    printf("Borrowing record added successfully!\n");
}

void viewBorrowings() {
    FILE *fp = fopen("../data/borrowings.dat", "rb");
    if (!fp) {
        printf("Error: No borrowings found!\n");
        return;
    }

    Borrowing b;
    printf("\n=== Borrowing List ===\n");
    while (fread(&b, sizeof(Borrowing), 1, fp)) {
        printf("ID: %d | Book ID: %d | Member ID: %d | Borrow Date: %s | Due Date: %s | Return Date: %s | Staff ID: %d\n",
               b.borrowing_id, b.book_id, b.member_id, b.borrow_date, b.due_date, b.return_date, b.staff_id);
    }

    fclose(fp);
}
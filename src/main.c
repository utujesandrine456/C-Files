#include <stdio.h>
#include <stdlib.h>
#include "../include/book.h"
#include "../include/author.h"
#include "../include/borrow.h"
#include "../include/fine.h"
#include "../include/member.h"
#include "../include/publisher.h"
#include "../include/staff.h"

// Function to clear the screen (platform-independent)
void clearScreen() {
    system("cls || clear");
}

// Function to pause and wait for user input
void pause() {
    printf("\nPress Enter to continue...");
    while (getchar() != '\n');
    getchar();
}

int main() {
    int choice;
    do {
        clearScreen();
        printf("\n=====================================\n");
        printf("       Library Management System      \n");
        printf("=====================================\n");
        printf("1. Add Book\n");
        printf("2. View Books\n");
        printf("3. Add Author\n");
        printf("4. View Authors\n");
        printf("5. Add Borrowing\n");
        printf("6. View Borrowings\n");
        printf("7. Add Fine\n");
        printf("8. View Fines\n");
        printf("9. Add Member\n");
        printf("10. View Members\n");
        printf("11. Add Publisher\n");
        printf("12. View Publishers\n");
        printf("13. Add Staff\n");
        printf("14. View Staff\n");
        printf("0. Exit\n");
        printf("=====================================\n");
        printf("Enter your choice: ");
        if (scanf("%d", &choice) != 1) {
            while (getchar() != '\n'); // Clear invalid input
            choice = -1; // Invalid choice
        }
        while (getchar() != '\n'); // Clear input buffer

        switch (choice) {
            case 1: addBook(); pause(); break;
            case 2: viewBooks(); pause(); break;
            case 3: addAuthor(); pause(); break;
            case 4: viewAuthors(); pause(); break;
            case 5: addBorrowing(); pause(); break;
            case 6: viewBorrowings(); pause(); break;
            case 7: addFine(); pause(); break;
            case 8: viewFines(); pause(); break;
            case 9: addMember(); pause(); break;
            case 10: viewMembers(); pause(); break;
            case 11: addPublisher(); pause(); break;
            case 12: viewPublishers(); pause(); break;
            case 13: addStaff(); pause(); break;
            case 14: viewStaff(); pause(); break;
            case 0: printf("Exiting system. Goodbye!\n"); break;
            default: printf("Invalid choice! Please try again.\n"); pause();
        }
    } while (choice != 0);
    return 0;
}
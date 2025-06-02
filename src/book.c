#include <stdio.h>
#include <string.h>
#include "../include/book.h"

void addBook() {
    FILE *fp = fopen("../data/books.dat", "ab");
    if (!fp) {
        printf("Error: Cannot open books file!\n");
        return;
    }

    Book b;
    printf("\n=== Add New Book ===\n");
    printf("Enter Book ID: "); scanf("%d", &b.book_id);
    while (getchar() != '\n'); // Clear input buffer
    printf("Title: "); fgets(b.title, 100, stdin); strtok(b.title, "\n");
    printf("Author ID: "); scanf("%d", &b.author_id);
    printf("Publisher ID: "); scanf("%d", &b.publisher_id);
    while (getchar() != '\n'); // Clear input buffer
    printf("ISBN: "); fgets(b.isbn, 20, stdin); strtok(b.isbn, "\n");
    printf("Genre: "); fgets(b.genre, 50, stdin); strtok(b.genre, "\n");
    printf("Year Published: "); scanf("%d", &b.year_published);
    printf("Copies Available: "); scanf("%d", &b.copies_available);
    while (getchar() != '\n'); // Clear input buffer
    printf("Shelf Location: "); fgets(b.shelf_location, 30, stdin); strtok(b.shelf_location, "\n");

    fwrite(&b, sizeof(Book), 1, fp);
    fclose(fp);
    printf("Book added successfully!\n");
}

void viewBooks() {
    FILE *fp = fopen("../data/books.dat", "rb");
    if (!fp) {
        printf("Error: Cannot open books file!\n");
        return;
    }

    Book b;
    printf("\n=== Book List ===\n");
    while (fread(&b, sizeof(Book), 1, fp)) {
        printf("ID: %d | Title: %s | Author ID: %d | Publisher ID: %d | ISBN: %s | Genre: %s | Year: %d | Copies: %d | Shelf: %s\n",
               b.book_id, b.title, b.author_id, b.publisher_id, b.isbn, b.genre, b.year_published, b.copies_available, b.shelf_location);
    }

    fclose(fp);
}
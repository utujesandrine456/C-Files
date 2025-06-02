#include <stdio.h>
#include <string.h>
#include "../include/author.h"

void addAuthor() {
    FILE *fp = fopen("../data/authors.dat", "ab");
    if (!fp) {
        printf("Error: Cannot open authors file!\n");
        return;
    }

    Author a;
    printf("\n=== Add New Author ===\n");
    printf("Enter Author ID: "); scanf("%d", &a.author_id);
    while (getchar() != '\n'); // Clear input buffer
    printf("Name: "); fgets(a.name, 100, stdin); strtok(a.name, "\n");
    printf("Bio: "); fgets(a.bio, 500, stdin); strtok(a.bio, "\n");

    fwrite(&a, sizeof(Author), 1, fp);
    fclose(fp);
    printf("Author added successfully!\n");
}

void viewAuthors() {
    FILE *fp = fopen("../data/authors.dat", "rb");
    if (!fp) {
        printf("Error: No authors found!\n");
        return;
    }

    Author a;
    printf("\n=== Author List ===\n");
    while (fread(&a, sizeof(Author), 1, fp)) {
        printf("ID: %d | Name: %s | Bio: %s\n", a.author_id, a.name, a.bio);
    }

    fclose(fp);
}
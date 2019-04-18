/*
Grijesh Chauhan
MNIT,Jaipur
Date:28-05-2012
grijesh.mnit@gmail.com

Objective: Q1 Without Using any CONDITIONAL STATEMENT [i.e if-else, switch] print the first EVEN DIGIT from the RIGHT, if exists else print -1.

Note: No input formate error is handle

compile:
    gcc -std=gnu99 -Wall -pedantic answer.c -o answer
*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char* argv[]) {

    FILE *ifp = NULL, *ofp = NULL;
    int ncases = 0, num = 0, count = 1, result = -1, remainder = 0;
        
    ifp = fopen(argv[1], "r");
    if(ifp == NULL){
        fprintf(stderr, "cannot open file '%s'\n", argv[1]);
        exit(EXIT_FAILURE);
    }
    ofp = fopen("q.out", "w");
    if(ofp == NULL){
        fprintf(stderr, "cannot open file 'q.out' \n");
        fclose(ifp);
        exit(EXIT_FAILURE);
    }
    fscanf(ifp, "%i", &ncases);
    fprintf(ofp,"%i\n", ncases);
    
    while(fscanf(ifp, "%i", &num) != EOF) {
        result = -1;
        do {
            remainder = num % 10;
            num /= 10;
            (void)(remainder % 2 || (result = remainder));
        } while(num && remainder % 2);
        
        fprintf(ofp, "CASE#%d = %i\n", count, result);
        ++count;
    }
    
    fclose(ifp);
    fclose(ofp);
    return EXIT_SUCCESS;
}

/*
Grijesh Chauhan
MNIT,Jaipur
Date:28-05-2012
grijesh.mnit@gmail.com

Objective: 
Summation of sequence of integers is always a common problem in Computer Science.
Rather than computing blindly, some intelligent techniques make the task simpler.
Here you have to find the summation of a sequence of integers. The sequence is an
interesting one and it is the all possible permutations of a given set of digits.
For example, if the digits are <1 2 3>, then six possible permutations are <123>,
<132>, <213>, <231>, <312>, <321> and the sum of them is 1332.

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define DEBUG 1


unsigned int factorial(int n) {
    unsigned int f = 1u;
    if(n == 0 || n == 1)
        return 1;
    while(n > 1)
        f *= n--;
    return f;
}

unsigned int summation(int digits[], int n){
    int i = 0, j = 0, digitsum = 0;
    unsigned result = 0u, tens = 1u, permutation = 0u;
    struct {
        int digits[9];
        int count[9];
    } repeat;
    int repeatcount = 0;
    for(i = 0; i < n; i++){
        for(j = 0; j < repeatcount; j++){
            if (digits[i] == repeat.digits[j]){
                repeat.count[j]++;
                break;
            }
        }
        if(j == repeatcount){
            repeat.digits[repeatcount] = digits[i];
            repeat.count[repeatcount] = 1;
            repeatcount++;
        }
    }
    permutation = factorial(n);
    for(j = 0; j < repeatcount; j++){
        permutation /= factorial(repeat.count[j]);
    }
    digitsum = 0;
    for(j = 0; j < repeatcount; j++){
        digitsum += repeat.count[j] * repeat.digits[j] * permutation / n;
    }
    for(result = 0u, i = 0; i < n; ++i){
        result += tens * digitsum;
        tens *= 10;
    }
    return result;
}

int main(int argc, char* argv[]) {

    FILE *ifp = NULL, *ofp = NULL;
    int ncases = 0, count = 1,
        N = 0, digits[9] = {0},
        i = 0;

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
    fscanf(ifp, "%i\n", &ncases);
    fprintf(ofp, "%i\n", ncases);
    
    while(ncases){
        fscanf(ifp, "%i\n", &N);
        for(i = 0; i < N && i < 9; i++){
            fscanf(ifp, "%d", &digits[i]);
            fgetc(ifp);
        }
#if DEBUG == 1
        printf("%d: ", N);
        for(i = 0; i < N; i++){
            printf("%d ", digits[i]);
        }
        printf("\n");
#endif
        fprintf(ofp, "CASE#%d = %u\n", count, summation(digits, N));
        --ncases;
        ++count;
    }
    fclose(ifp);
    fclose(ofp);
    return EXIT_SUCCESS;
}

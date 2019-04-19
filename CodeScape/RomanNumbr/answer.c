/*
	Grijesh Chauhan
	MNIT,Jaipur
	Date:28-05-2012
	grijesh.mnit@gmail.com
	
	Objective: Write a program to convert positive integer, represented in 
	ENGLISH LANGUAGE format ( eg. 1234 is integer represented in ENGLISH 
	LANGUAGE is ONE THOUSAND TWO HUNDRED THIRTY FOUR) into Roman numbers.
	
	Note:  No input formate error is handle!!
	    ** Please take care of spelling mistake
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *ones[] = { 
	"",
	"one",
	"two",
	"three",
	"four",
	"five",
	"six",
	"seven",
	"eight",
	"nine",
	"ten",
	"eleven",
	"twelve",
	"thirteen",
	"fourteen",
	"fifteen",
	"sixteen",
	"seventeen",
	"eighteen",
	"nineteen",
};			   
char *tens[] = {
	"",
	"",
	"twenty",
	"thirty",
	"forty",
	"fifty",
	"sixty",
	"seventy",
	"eighty",
	"ninety",
};
             
int wordtodigit(char *s){
	int i = 0;
	for(i = 1; i < 20; ++i){
		if(strcasecmp(ones[i], s) == 0)
			return i;
	}
	for(i = 2; i < 10; ++i){
		if(strcasecmp(tens[i], s) == 0)
			return i * 10;
	}
	if(strcasecmp("hundred", s) == 0)
		return 100;
	if(strcasecmp("thousand", s) == 0)
		return 1000;
	return 0;
}

int engtonum(char *s){
	int last_digit = 0, digit = 0, number = 0;
	char *token = NULL;
	
	for(token = strtok(s, " "); token; token = strtok(NULL, " ")){
		digit = wordtodigit(token);
		if(digit < 100){
			last_digit = digit;
			number += last_digit;
		}
		if(digit == 100){
			if(last_digit){
				number -= last_digit;
				last_digit *= 100;
			}
			number += last_digit;
		}
		if(digit == 1000)
			number *= 1000;
	}
	return number;
}

void numtoroman(int number, char* roman){
	int left_digit = 0, i = 0;
	roman[0] = 0;
	if(number == 0)
		return;
	if(number >= 1000){
		left_digit = number / 1000;
		for(i = 1; i <= left_digit; i++){
			strcat(roman, "m");
		}
		number -= left_digit * 1000;
	}
	if(number >= 900){
		strcat(roman, "cm");
		number -= 900;
	}
	if(number >= 500){
		strcat(roman, "d");
		number -= 500;
		left_digit = number / 100;
		for(i = 1; i <= left_digit; i++){
			strcat(roman, "c");
		}
		number -= left_digit * 100;
	}
	if(number >= 400){
		strcat(roman, "cd");
		number -= 400;
	}
	if(number >= 100){
		left_digit = number / 100;
		for(i = 1; i <= left_digit; i++){
			strcat(roman, "c");
		}
		number -= left_digit * 100;
	}
	if(number >= 90){
		strcat(roman, "xc");
		number -= 90;
	}
	if(number >= 50){
		strcat(roman, "l");
		number -= 50;
		left_digit = number / 10;
		for(i = 1; i <= left_digit; i++){
			strcat(roman, "x");
		}
		number -= left_digit * 10;
	}
	if(number >= 40){
		strcat(roman, "xl");
		number -= 40;
	}
	if(number >= 10){
		left_digit = number / 10;
		for(i = 1; i <= left_digit; i++){
			strcat(roman, "x");
		}
		number -= left_digit * 10;
	}
	if(number == 9){
		strcat(roman, "ix");
	}
	if(number >= 5){
		strcat(roman, "v");
		number -= 5;
		while(number){
			strcat(roman, "i");
			number--;
		}
	}
	if (number == 4){
		strcat(roman, "iv");
		return;
	}
	while(number){
		strcat(roman, "i");
		number--;
	}
}

void debug(char* lineptr, int linelen){
	int number = 0;
	char roman[128] = "";
	printf("%d: %s: ", linelen, lineptr);
	number = engtonum(lineptr);
	numtoroman(number, roman);
	printf("%d: %s", number, roman);
	printf("\n");
}

int main(int argc, char* argv[]){

	FILE *ifp = NULL, *ofp = NULL;
	int ncases = 0, count = 1;
	size_t linelen = 0, len = 0;
	char* lineptr = NULL;
	char roman[128] = "";
	
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
    fprintf(ofp,"%i\n", ncases);
    
    while((linelen = getline(&lineptr, &len, ifp)) != -1){
    	if (lineptr[linelen - 1] == '\n'){
    		lineptr[linelen - 1] = '\0';
    		linelen -= 1;
    	}
    	numtoroman(engtonum(lineptr), roman);
    	fprintf(ofp, "CASE#%d= %s\n", count, roman);
    	count++;
    }
    free(lineptr);
    exit(EXIT_SUCCESS);
}

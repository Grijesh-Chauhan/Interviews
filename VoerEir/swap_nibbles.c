/* Swap nibbles in 1 byte unsigned number
   
   gcc -std=gnu99 -Wall -Os -pedantic swap_nibbles.c -o swap_nibbles
*/

#include<stdio.h>
#include<stdlib.h>
#include<stdint.h>

uint8_t swap_nibbles(uint8_t num) {
    return (num & 0xF0) >> 4 | (num & 0x0F) << 4;
}

int main(int argc, char* argv[]) {
    uint8_t num = 0xBC;  // 0b1011 1100
    printf("swap_nibbles(%x) -> %x", num, swap_nibbles(num));
    printf("\n");    
    return EXIT_SUCCESS;
}

// other questions:
// what is `uint8_t`?
// what is size of char and 'A'



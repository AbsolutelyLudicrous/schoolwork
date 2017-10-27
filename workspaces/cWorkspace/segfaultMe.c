#include <stdio.h>
#include <string.h>
int main(){	printf("S E G F A U L T\n");
		memset((char *)0x0, 1, 100);
		return 0;}

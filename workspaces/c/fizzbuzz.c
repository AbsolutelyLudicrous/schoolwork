#include <stdio.h>

void main(){
	int i = 1;
	for ( i ; i <= 100 ; i++ ){
		if( i % 3 == 0 )
			{printf("fizz\n");}
		if( i % 5 == 0 )
			{printf("buzz\n");}
		if(!( i % 5 == 0 ) && !( i % 3 == 0 ))
			{printf("%d\n",i);}
	}
}

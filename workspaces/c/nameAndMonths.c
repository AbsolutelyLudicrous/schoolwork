#include <stdio.h>

int main(){
	char name0 [64] = "Foo";
	char name1 [64] = "Bar";

	//using these in place of scanfs
	
	int years0 = 15;
	int month0 = 2;

	int years1 = 16;
	int month1 = 2;

	//printf("%s is %d months old\n", &name0, (years0 * 12 + month0));
	//printf("%s is %d months old\n", &name1, (years1 * 12 + month1));

	//printf("Function pass attempt\n");
	
	printTheString(name0,years0,month0);
	printTheString(name1,years1,month1);
}
void printTheString(char name[], int years, int month){
	printf("%s is %d months old\n", name, (years * 12 + month));
}

/*
 * can sizeof take variable or types?
 *
 * sizeof and min/max of ints and longs
 */

#include <stdio.h>

void main () {
	unsigned int uint = 1;
	int sint = 1;

	unsigned long ulong = 1;
	long slong = 1;

	//unsigned float ufloat = 1;
	float sfloat = 1;

	//unsigned double udouble = 1;
	double sdouble = 1;

	printf("unsinged int, given a value: %d\n",sizeof(uint));
	printf("int, given a value: %d\n",sizeof(sint));
	printf("unsigned long, given a value: %d\n",sizeof(ulong));
	printf("long, given a value: %d\n",sizeof(slong));
	//printf("unsigned float, given a value: %d\n",sizeof(slong));
	printf("float, given a value: %d\n",sizeof(slong));
	//printf("unsigned double, given a value: %d\n",sizeof(slong));
	printf("double, given a value: %d\n",sizeof(slong));

	printf("unsigned int: %d\n",sizeof(unsigned int));
	printf("int: %d\n",sizeof(int));
	printf("unsinged long: %d\n",sizeof(unsigned long));
	printf("long: %d\n",sizeof(long));
	//printf("unsigned float: %d\n",sizeof(unsigned float));
	printf("float: %d\n",sizeof(float));
	//printf("unsigned double: %d\n",sizeof(unsigned double));
	printf("double: %d\n",sizeof(double));
}

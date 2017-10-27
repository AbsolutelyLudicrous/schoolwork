#include <stdio.h>

struct human {
	int years;
	int months;
};

int main(){
	struct human Foo, Bar;
	Foo.years = 123;
	Foo.months = 456;

	Bar.years = 789;
	Bar.months = 101;

	baz(Foo, Bar);
}
void baz(struct human a, struct human b){
	int aHours = a.years * 365 * 24 + a.months * 30 * 24;
	int bHours = b.years * 365 * 24 + b.months * 30 * 24;
	printf("%d\n", aHours);
	printf("%d\n", bHours);
}

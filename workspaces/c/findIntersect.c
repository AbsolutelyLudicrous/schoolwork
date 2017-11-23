#include <stdio.h>
/*
 * Solves linear systems of equations.
 * Runtime:O(n^2)
 * TODO:Add quadratic support
 * TODO:Lower runtime
 */
int main(){
	int slope1; int slope2;	//slope of line
	scanf("Slope of the primary equation: %d", slope1);
	scanf("Slope of the secondary equation: %d", slope2);

	int yoff1; int yoff2;	//y-offset
	scanf("Y-Offset of the primary equation: %d", yoff1);
	scanf("Y-Offset of the secondary equation: %d", yoff2);

	int domainStart; int domainEnd;	//indicates where we start and begin our search
	scanf("Domain starts: %d", domainStart);
	scanf("Domain ends: %d", domainEnd);

	for(domainStart; domainStart<domainEnd; domainStart++){	//we use the domainStart variable to conserve memory, it acts as an x value on a graph
		int val1;	//value of the primary equation at current x value
		int val2;	//value of the secondary equation at current x value

		val1=(slope1*domainStart)+yoff1;
		int forw = domainStart+1;
		for(forw;forw<domainEnd;forw++){	//check all x values ahead of current
			val2=(slope2*forw)+yoff2;
			if(val1==val2){
				printf("Found: %d");
			}
		}
	}
	return 0;
}

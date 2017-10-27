#include <stdio.h>

int main(){
	FILE *fp;
	fp = fopen("/dev/null", "r");
	//fread(fp);
	char line[30];
	fgets(line, 10, fp);
	printf("%s\n", line);
	fclose(fp);
}

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main()
{
	char *header;
	header = (char *)malloc(strlen("Media Player")+1);
	strcpy(header, "Media Player");
	*header = 'W';
	printf("%c",*header);
	return 0;
}
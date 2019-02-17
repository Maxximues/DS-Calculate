#include<stdio.h>
#define M 3
int main(){
	int i=0, k=M-1;
	char *w = {"ABCDEFGHIJK"};
	char *temp=w;
	while(*w){*temp=w[k];k++;temp++;}
	for(k=0; k<M; k++){*temp=w[k];temp++;}
	temp[i]='\0';
	w=temp;
	while(*w!='\0'){printf("%c", *w);w++;}
	return 0;
}

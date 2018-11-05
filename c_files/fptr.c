#include<stdio.h>
typedef int (*fptrOperation)(int, int);

int main(){
	int compute(fptrOperation operation, int num1, int num2);
	int subtract(int num1, int num2);
	int add(int num1, int num2);

	printf("%d\n",compute(add, 5, 6));
	printf("%d\n",compute(subtract, 5, 6));
	return 0;
}

int add(int num1, int num2){
	return (num1 + num2);
}

int subtract(int num1, int num2){
	return (num1 - num2);
}

int compute(fptrOperation operation, int num1, int num2){
	return operation(num1, num2);
}

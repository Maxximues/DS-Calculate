#include<stdio.h>
#include<stdlib.h>
#define Stack_init_size 5
#define Stack_increasment 10

typedef struct Stack{ 
	int *base;
	int top;
	int stacksize;
}Stack, *StackPtr;

int main(){
	Stack s;
	int len;
	int Pop(StackPtr S);
	_Bool isEmpty(StackPtr S);
	StackPtr InitStack(StackPtr S);
	StackPtr Pushelem(StackPtr S, int len);
	StackPtr Display(StackPtr S);
	StackPtr Empty(StackPtr S);


	printf("len: \n");
	scanf("%d", &len);
	InitStack(&s);
	Pushelem(&s, len);
	Display(&s);
	printf("top elem %d wased poped\n", Pop(&s));
	if(isEmpty(&s)) printf("Stack is Emptied\n");
	else {
		printf("Stack is not empty\n");
		Empty(&s);
	}	
	if(isEmpty(&s)) printf("Stack is Emptied\n");


	return 0;
}
 
StackPtr InitStack(StackPtr S){
	printf("Success in InitStack\n");
	S->base = (int *)malloc(sizeof(int) * Stack_init_size);
	if(!S->base) exit(1);
	S->top = -1;
	S->stacksize = Stack_init_size;
	return S;
}

StackPtr Pushelem(StackPtr S, int len){
	if(len >= Stack_init_size){
		S->base = (int *)realloc(S->base, sizeof(int) * (S->stacksize + Stack_increasment));
		S->stacksize += Stack_increasment;
	}
	if(!S->base) exit(1);
	printf("Success in Pushelem\n");
	for(S->top = 0; S->top < len; S->top++){
		printf("elem: \t");
		scanf("%d", &S->base[S->top]);
	}
	return S;
}

StackPtr Display(StackPtr S){
	int i;

	printf("From top to base\n");
	for(i = S->top - 1; i >= 0; i--){
		printf("%d\n", S->base[i]);
	}
}

int Pop(StackPtr S){
	int *popelem;

	popelem = (int *)malloc(sizeof(int));
	*popelem = S->top;
	--S->top;
	return *popelem;

}

_Bool isEmpty(StackPtr S){
	if(S->top == -1)
		return 1;
	return 0;
}

StackPtr Empty(StackPtr S){
	S->top = -1;
	return S;
}
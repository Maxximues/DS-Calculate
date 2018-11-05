#include<stdio.h>
#include<stdlib.h>
typedef struct QNode{
	int data;
	struct QNode *next;
}QNode, *QNodePtr;
typedef struct{
	QNodePtr front;
	QNodePtr rear;
}LinkQuene, *Ptr;
int main(){
	int len, i;
	LinkQuene Q;
	Ptr EnQuene(Ptr Q);
	Ptr InitQuene(Ptr Q);
	Ptr OutQuene(Ptr Q);
	void EmptyQuene(Ptr Q);
	
	InitQuene(&Q);
	printf("len:\t");
	scanf("%d", &len);
	for(i = 0; i < len; i++)
		EnQuene(&Q);
	OutQuene(&Q);
	EmptyQuene(&Q);
	EnQuene(&Q);
	return 0;
}

Ptr InitQuene(Ptr Q){
	printf("in InintQuene\n");
	Q->front = Q->rear = (QNodePtr)malloc(sizeof(QNode));
	if(!Q->front) exit(1);
	Q->front->next = NULL;
	return Q;
}

Ptr EnQuene(Ptr Q){
	QNodePtr NewNode;
	
	printf("in EnQuene\n");
	NewNode = (QNodePtr)malloc(sizeof(QNode));
	if(!NewNode) exit(1);
	printf("data: \t");
	scanf("%d", &NewNode->data);
	NewNode->next = NULL;
	if(Q->front == Q->rear){
		Q->front->next = NewNode;
		Q->rear = NewNode;
	}
	else{
	Q->rear->next = NewNode;
	Q->rear = NewNode;
	}
	printf("%d,%d\n", Q->front->next->data,Q->rear->data);
	return Q;
}

Ptr OutQuene(Ptr Q){
	QNodePtr P;

	printf("in OutQuene\n");
	if(Q->front->next == Q->rear) exit(1);
	P = Q->front->next;
	Q->front->next = P->next;
	if(Q->rear == P) Q->rear = Q->front;
	free(P);
	P = NULL;
	printf("%d,%d\n",Q->front->next->data,Q->rear->data);
	return Q;
}

void EmptyQuene(Ptr Q){
	QNodePtr clear;
	printf("Now all Quene will be emptied!\n");
	clear = Q->front->next;
	while(clear){
		free(clear);
		Q->front = Q->front->next;
		clear = Q->front->next;
	}
}

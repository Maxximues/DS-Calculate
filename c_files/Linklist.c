#include<stdio.h>
#include<stdlib.h>

typedef struct Node{
	int data;
	struct Node* next;
}Node, *Ptr;
typedef Ptr *SecPtr;

int main(){
	Ptr p;
	int len, position;
	Ptr InitLink(int len);
	void Display(Ptr headNode);
	Ptr Insert(Ptr headNode, int pos);
	Ptr ListDelet(Ptr headNode, int pos);

	printf("len: ");
	scanf("%d", &len);
	p = InitLink(len);
	Display(p);
	printf("Insert position:\n");
	scanf("%d", &position);
	Display(Insert(p, position));
	printf("Insert Deletposition:\n");
	scanf("%d", &position);
	Display(ListDelet(p, position));
	
}
Ptr InitLink(int len){
	Ptr n1, n2, headNode;
	int j = 0;
	headNode = NULL; 
	n1 = (Ptr)malloc(sizeof(Node));
	printf("Node->data: ");
	scanf("%d", &n1->data);
	n1->next = NULL;
	headNode = n1;
	j++;
	while(j < len){
		n2 = (Ptr)malloc(sizeof(Node));
		printf("Node->data: ");
		scanf("%d", &n2->data);
		n1->next = n2;
		n1 = n2;
		j++;
		n1->next = NULL;
	}
	return headNode;
}

void Display(Ptr headNode){
	Ptr head;

	head = headNode;
	printf("in Display: \n");
	while(head != NULL){
		printf("%d\t", head->data);
		head = head->next;
	}
	printf("\n");
}

Ptr Insert(Ptr headNode, int pos){
	Ptr head, newNode, headnew;
	int newdata;

	headnew = headNode;
	head = headNode;
	while(head && head->next && head->next->data != pos){
		head = head->next;
	}
	newNode = (Ptr)malloc(sizeof(Node));
	printf("newdata: \n");
	scanf("%d", &newNode->data);
	newNode->next = head->next;
	head->next = newNode;
	return headnew;
}

Ptr ListDelet(Ptr headNode, int pos){
	Ptr head, headnew, DeletNode;

	head = headNode;
	headnew = headNode;
	if(head->data = pos){
		DeletNode = head;
		headnew = head->next;
	}
	else{
		while(head->next->data != pos)
			head = head->next;
		DeletNode = head->next;
		head->next = head->next->next;
	}
	free(DeletNode);
	return headnew;
}
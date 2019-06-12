#include<stdio.h>
#define N 100
int heap[N];

int main(){
	int i, num;
	int create(int num);
	int sfitdown(int i, int num);
	int swap(int i, int min);
	int deletemax(int num);

	printf("input num: ");
	scanf("%d", &num);

	for(i=1; i<=num;i++){
		scanf("%d", &heap[i]);
	}

	create(num);

	for(i=1; i<=num;i++){
		printf("%3d", deletemax(num));
	}
	return 0;
}

int swap(int i, int min){
	int tmp;
	tmp = heap[i];
	heap[i]=heap[min];
	heap[min]=tmp;
	return 0;
}

int siftdown(int i, int num){
	int flag=0, min;

	while(i*2<=num && flag==0){
		if(heap[i] > heap[i*2])min = i*2;
		else min = i;
		if(heap[min] > heap[i*2+1])min = i*2 +1;
		if(min != i){
			swap(i, min);
			i = min;
		}
		else flag = 1;
	}
	return 0;
}

int create(int num){
	int i;

	for(i=num/2; i>=1; i--){
		siftdown(i, num);
	}
	return 0;
}

int deletemax(int num){
	int t;
	t = heap[1];
	heap[1] = heap[num];
	num--;
	siftdown(1, num);
	return t;
}

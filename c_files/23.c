#include<stdio.h>
#include<math.h>
int main(){
	/*int n; double S=1.0, x, k=1.0;
	int i;
	scanf("%lf", &x);
	scanf("%d", &n);
	for(i=1; i<=n; i++){
		for(k=1; k<=i; k++)
			k *= k;
		S += pow(x, i)/k;
	}*/
	int n;
	double x;
	int i; double s=1.0, s1=1.0;
	scanf("%d", &n);
	scanf("%lf", &x);
	for(i=1; i<=n; i++){
		s1=s1*i;
		s=s+pow(x, i)/s1;
	}
	printf("%lf", s);
	return 0;
}


#include<stdio.h>
 int swap(int a,int b)
 {
 	int tam=0;
 	tam=a;
 	a=b;
 	b=tam;
 	printf("\n after swap:a=%d,b=%d",a,b);
}
  int main()
{
	int a,b;
	printf("nhap a =",a);
	scanf("%d",&a);
	printf("nhap b =",b);
	scanf("%d",&b);
	swap(a,b);
}


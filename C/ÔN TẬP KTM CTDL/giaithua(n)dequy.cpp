#include <stdio.h>
 
long long fact(int n) 
{
    if(n == 0) 
	return 1;
    return n * fact(n-1);
}
 
int main()
{
    int n;
 
    printf("nhap n = ");
    scanf("%d", &n);
 
    printf("giai thua cua %d! = %lld\n", n, fact(n));
 
    return 0;
}

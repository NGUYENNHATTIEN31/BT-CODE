#include <stdio.h>
int fibonacci(int n)
{
    if (n==1||n==2)
        return 1;
    return fibonacci(n-1)+fibonacci(n-2);
}
int main()
{
    int n;
    printf("nhap so thang can tinh=%",n);
    scanf("%d", &n);
    printf("tong so cap sau %d thang la%d", n, fibonacci(n));
}

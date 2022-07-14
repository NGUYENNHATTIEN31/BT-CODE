# include<stdio.h>
# include<string.h>

int fibonacci(int val)
{
	if(val<0)
	{
		return -1;
	}
	else if(val==0 ||val==1)
	{
		return val;
	}
	else
	{
		return fibonacci(val - 1)+fibonacci(val - 2);
	}
}
int main()
{
	float inputNum;
	int i;
	printf("\nNhap so phan tu trong day Fibo:");
	scanf("%f",&inputNum);
	
	printf("Day so Fibo cua ban la: \n");
	for (i=0;i< inputNum;i++)
	{
		printf("%d ",fibonacci(i));
	}	
	return 0;
	
}

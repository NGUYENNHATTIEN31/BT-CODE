#include<stdio.h>
void Nhapmang(int a[],int n)
{
	for(int i = 0;i< n; ++i)
	{
		printf("Nhap phan tu a[%d] =",i);
		scanf("%d",&a[i]);
	}
}
void selection_sort(int a[],int n)
{
	int i,j,min,temp;
	for (i=0;i<n-1;i++)
	{
		min=i;
		for(j=i+1;j<n;j++)
		{
			if(a[j]<a[min])
			min=j;
		}
		temp=a[i];
		a[i]=a[min];
		a[min]=temp;
	}
	
}
void insertion_sort(int a[],int n)
{
	int i,j,tmp;
	for(i=1;i<n;i++)
	{
		j=i-1;
		tmp=a[i];
		while(tmp<a[j]&&j>=0)
		{
			a[j+1]=a[j];
			j--;
		}
		a[j+1]=tmp;
	}
}	
void bubble_sort(int a[],int n)
{
	int i,j,tmp;
	for (i=0;i<n-1;i++)
	{
		for (j=n-1;j>i;j--)
		{
			if(a[j]<a[j-1])
			{
				tmp=a[j-1];
				a[j-1]=a[j];
				a[j]=tmp;
			}
		}	
	}
}	
void Xuatmang( int a[],int n)
{
	for (int i =0;i<n;++i)
	{
		printf("%d\t",a[i]);
	}
}
int main()
{
//	int n;
//	int a[n];
//	printf("nhap so luong phan tu trong mang=");
//	scanf("%d",&n);
//	for(int i=0;i<n;i++)
//	{
//		printf("nhap phan tu thu a[%d]=",i);
//		scanf("%d",&a[i]);
//	}
//	
//	printf("mang tang dan:\t");
//	selection_sort(a,n);
//	Xuatmang(a,n);
	int a[50];
	int n;
	do
	{
		printf("Nhap so luong phan tu ");
		scanf("%d",&n);
	}
	while (n<=0 || n>=50);
	Nhapmang(a,n);
	printf("sap xep chon la:\t");
	selection_sort(a,n);
	Xuatmang(a,n);
	printf("\n\n");
	printf("sap xep chen la:\t");
	insertion_sort(a,n);
	Xuatmang(a,n);
	printf("\n\n");
	printf("sap xep noi bot la:\t");
	bubble_sort(a,n);
	Xuatmang(a,n);
	
}



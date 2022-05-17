#include<stdio.h>
 int main()
 {	/*khai báo mang*/
 	int n;
 	printf("nhap so phan tu:");
 	scanf("%d",&n);
 	int a[50];
 	
    for(int i=0;i<n;i++)
    {
    	printf("nhap phan tu cua a[%d]=",i);
    	scanf("%d",&a[i]);
	}
    /*sap xep mang*/
    int trunggian;
    for (int i=0;i<n-1;i++)
    {
    	for (int j=i+1;j<n;j++)
    	{
    		if(a[i]>a[j])
    		{
    			trunggian=a[i];
    			a[i]=a[j];
    			a[j]=trunggian;
    		}
    	}
    }
    for(int i=0;i<n;i++)
    {
    	printf("%d\n",a[i]);
    }
    
    
    			
    			
}

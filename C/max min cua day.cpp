#include<stdio.h>
void nhap(int a[],int n)
{
	for (int i=0;i<n;i++)
	{
		printf("nhap vao phan tu a[%d]:",i);
		scanf("%d",&a[i]);
		}
}
int main(){
	
		int max=a[0],min=a[0];
		for(int i=1;i<n;i++)
		{
			if(max<a[i]){
			 max=a[i];
			}
			if(min>a[i]){
			 min=a[i];
			}
		}
		return max,min;
    
    }
 		

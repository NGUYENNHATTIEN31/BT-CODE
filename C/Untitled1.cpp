#include<stdio.h>
int main()
{
 int i,size;
 int sum;
 printf("Nhap vao so phan tu cua mang:\n");
 scanf("%d",&size);
 int a[size];
 for(i=0;i<(size);i++){
  printf("Nhap gia tri cho phan tu thu %d: ",i);
  scanf("%d",&a[i]);
 }
 sum=0;
 for(i=0;i<size;i++){
  if(a[i]%2==0){
   sum = sum + a[i];
  } 
 }
 printf("%d",sum);
}


#include<stdio.h>
 int main(){
 int size;
 printf("Nhap so pt cua mang:\n");
 scanf("%d",&size);
 int a[size];
  
 for(int i=0;i<=size;i++){
 printf("Gia tri phan tu a[%d]=", i);
 scanf("%d", &a[i]);
 }
 for(int i=0;i<=size;i++){
 printf("%d", a[i]);
 }
  
 }
 
 

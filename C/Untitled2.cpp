#include<stdio.h>
int main(){
 int i,s;
 int sum;
 printf("\nNhap so phan tu:");
 scanf("%d", &s);
 int a[s];
 for(i = 0; i < (s); i++){
  printf("Nhap gia tri %d: ",i);
  scanf("%d", &a[i]);
 }
 sum=0;
 for(i = 0;i < s; i++){
  sum = sum + a[i];
 }
 printf("%d",sum);
 
}

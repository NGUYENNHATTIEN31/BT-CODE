#include<stdio.h>
#include<math.h>
 int main()
 {
 	int a,b,c,denta ;
 	float x1,x2;
 	scanf("%d%d%d",&a,&b,&c);
 	printf("nhap a=%d\n",a);
 	printf("nhap b=%d\n",b);
 	printf("nhap c=%d\n",c);
    denta=b*b-4*a*c;
    printf("denta=%d\n",denta);
    if(denta<0)
    {
    	printf("phuong trinh vo nghiem");
    }
    else if(denta==0)
    {
    	printf("phuong trinh co nghiem kep x1=x2=%f",-b/2*a);
    }
    else
    {
    	x1=(-b+sqrt(denta))/2*a;
    	x2=(-b-sqrt(denta))/2*a;
    	printf("phuong trinh co 2 nghiem phan biet x1=%0.2f,x2=%0.2f",x1,x2);
    }
}
    

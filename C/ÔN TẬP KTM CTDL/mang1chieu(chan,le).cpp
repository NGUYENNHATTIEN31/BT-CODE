#include<stdio.h>
/*dinh nghia 1 cau truc NODE:khai bao*/
struct NODE{
	int data;
	struct NODE *pNext;
};

//typedef struct NODE*node;
/*dinh nghia 1 cau truc LIST: kha b?o */
struct LIST{
	NODE*pHead;
	NODE*pTail;
}; 

/*khoi tao 1 ds rong*/
void Init(LIST&l){
	l.pHead=l.pTail=NULL;
};
/* tao 1 node bat ki*/
NODE* CreateNode()
{
	int x;
	printf("nhap gia tri cho node: ");
	scanf("%d",&x);
	NODE *p=new NODE;
	p->data=x;
	p->pNext=NULL;
	return p;
}
/*chèn node vao cuoi ds*/
void  AddTail(LIST &l,NODE *p)
{
	if(l.pHead==NULL)
		l.pHead=l.pTail=p;
	else
	{
		l.pTail->pNext=p;
		l.pTail=p;
	}
	
}
void xuatchan(LIST &l)
{
	NODE*p=l.pHead;
	while(p)
	{
		if(p->data%2==0)
			printf("%d->",p->data);
		p=p->pNext;
	}
}	
		
void xuatle(LIST &l)
{
	NODE*p=l.pHead;
	while(p)
	{
		if(p->data%2!=0)
			printf("%d->",p->data);
		p=p->pNext;
	}
}	
int main()
{
	LIST l;
	Init(l);
	int n;
	printf("nhap so luong phan tu cua danh sach:");
	scanf("%d",&n);
	int i=1;
	while(i<=n)
	{
		NODE *p=new NODE;
		p=CreateNode();
		AddTail(l, p);
		i++;
	}
	printf("ds vua nhap la:");
	for (NODE *p=l.pHead;p!=NULL;p=p->pNext)
		printf("%d\t",p->data);
	printf("cac so chan");
	xuatchan(l);
	printf("\tcac so le");
	xuatle(l);
	
	
}


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
/*chen node vao dau ds*/
void  AddHead(LIST &l,NODE *p)
{
	if(l.pHead==NULL)
		l.pHead=l.pTail=p;
	else
	{
		p->pNext=l.pHead;
		l.pHead=p;
	}
	
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
//xoa 1 node dau ds
void DeleteHead(LIST &l)
{
	NODE *p=new NODE;
	p=l.pHead;
	l.pHead=l.pHead->pNext; //cap nhat lai node dau ds
	p->pNext=NULL; //go ket noi node p
	delete p; //xoa node p
}
//xoa 1 node cuoi ds
void  DeleteTail(LIST &l)
{
	for(NODE *k = l.pHead; k != NULL; k = k ->pNext)
	{
		if(k->pNext == l.pTail)
        {
           
            delete l.pTail;//xoa di phan tu cuoi
           	k->pNext = NULL;//cho con tro cua node ke cuoi tro den vung nho null
            l.pTail = k;//cap nhat lai l.pTail
        }
					
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
		
	printf("ds da xoa phan tu cuoi:");
	DeleteTail(l);
	for (NODE *p=l.pHead;p!=NULL;p=p->pNext)
		printf("%d\t",p->data);
	
	
	
	
}

 




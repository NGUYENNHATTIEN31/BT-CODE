struct NODE{
	int data;
	struct node*pNext;
};
typedef struct NODE*node;

struct list{
	node*phead;
	node*ptail;
}; 
typedef struct list*list;

void init(list&i){
	i.phead=i.ptail=null;
};

int x;
printf("nhap x=%d");
scanf("%d",x)
typedef sruct linkedlist*node;
node createnode(int value){
	node p;
	p=(node)malloc(sizeof(struct linkedlist));
	p->data=x;
	p->pNext=Null;
	return p;
}
	

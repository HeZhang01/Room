#include <stdio.h>
#include <stdlib.h>

/**
 * @author hezhang  
 * @time   2016/08/24
 * @brief  LRU算法是一种页面置换算法，其按照时间局部性的原则，认为在最近被访问的块(Page)在未来也有很高的概率被访问
 */
/* define node and basic list method*/
struct node
{
	int key;
	int val;
	struct node *before;
	struct node *after;
};

void initList(struct node *Node)
{
	Node->before = Node;
	Node->after  = Node;
}

void inList(struct node *list,struct node *newNode)
{
	if(!list)
		return;
	list->after->before = newNode;
	newNode->after = list->after;
	list->after = newNode;
	newNode->before = list;

}


struct node *outList(struct node *list,int key)
{
	if(!list)
		return NULL;
	struct node *currNode = list->after;
	while(currNode != list)
	{
		if(currNode->key == key )
		{
			currNode->after->before = currNode->before;
			currNode->before->after = currNode->after;
			inList(list,currNode);
			return currNode;
		}
		currNode = currNode->after;
	}
	return NULL;
}

/* LRU */
void set(int key, int val, struct node *list)
{
	struct node *newNode = (struct node *)malloc( sizeof(struct node) );
	newNode->key = key;
	newNode->val = val;
	newNode->before = NULL;
	newNode->after  = NULL;
	inList(list,newNode);
}

int get(int key, struct node *list)
{
	struct node *Node = outList(list,key);
	if(NULL == Node)
		return -1;
	return Node->val;
}

int main()
{
	struct node *list = (struct node *)malloc( sizeof(struct node) );
	initList(list);
	
	set(1,11,list);
	set(2,22,list);
	printf("%d, %d\n",list->after->key,list->after->val);
	printf("%d, %d\n",list->after->after->key,list->after->after->val);
	printf("%d, %d\n",list->after->after->after->key,list->after->after->after->val);
	printf("%d, %d\n",list->after->after->after->after->key,list->after->after->after->after->val);
	
	get(1,list);
	printf("%d, %d\n",list->after->key,list->after->val);
	printf("%d, %d\n",list->after->after->key,list->after->after->val);
	return 0;
}


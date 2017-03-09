#include <stdio.h>
#include <stdlib.h>

/**
 * @author hezhang
 * @time 2016/09/12 16:14:30
 * @brief 使用栈实现一个查找当前栈中最大元素的方法，要求时间复杂度为O(1)
 */
/* 节点定义 */
struct node {
	int data;
	struct node *next;
};

/* 栈是否为空 */
int isEmpty(struct node *s)
{
	return (s->next == NULL) ? 1 : 0;
}

struct node* getMax(struct node *s)
{
	return s->next;
}

/* 元push */

void _push(struct node *s, int data)
{
	if(s)
	{
		struct node *newNode = (struct node *)malloc( sizeof(struct node) );
		newNode->data = data;
		newNode->next = s->next;
		s->next       = newNode; 
	}
}

/* push方法 */
void push(struct node *s1, struct node *s2,int data)
{
	int current;
	if( !isEmpty(s1) )
	{
		struct node *max = getMax(s2);
		current = max->data > data ? max->data : data;
	}else
	{
		current = data;
	}

	_push(s1, data);
	_push(s2, current);
}

int main()
{
	struct node *s1 = (struct node *)malloc( sizeof(struct node) );
	struct node *s2 = (struct node *)malloc( sizeof(struct node) );
	push(s1, s2, 2);
	printf( "%d \n",getMax(s2)->data );
	push(s1, s2, 1);
	printf( "%d \n",getMax(s2)->data );
	push(s1, s2, 4);
	printf( "%d \n",getMax(s2)->data );
	push(s1, s2, 7);
	printf( "%d \n",getMax(s2)->data );
	push(s1, s2, 0);
	printf( "%d \n",getMax(s2)->data );
	
}

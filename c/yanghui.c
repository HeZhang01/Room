#include <stdio.h>
#include <>

/**
 * @author hezhang
 * @time 2016/9/19 16:47
 * @brief 打印杨辉三角的系数
 */

void yanghui(int n)
{
	int p[10][100];
	int i,j;
	p[0][0] = 0;
	p[0][1] = 1;
	p[0][2] = 0;
//	printf("1\n");
	for(i=1; i<=n; i++)
	{
		p[i][0] = 0;
		p[i][i+2] = 0;
		for(j=1;j<i+1;j++)
		{
			p[i][j] = p[i-1][j-1] + p[i-1][j];
			printf("%d ",p[i][j]);
		}
		printf("\n");
	}
	
}

int main()
{
return 0;
}

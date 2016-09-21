#include <queue>
#include <iostream>

/**
 * @brief 打印杨辉三角
 * @author hezhang
 * @time 2016/9/19 18:12
 * */

using namespace std;

void yanghui(int n)
{
	queue<int> q;
	q.push(0);
	q.push(1);
	cout << 1 << "\n";
	
	/* 行循环 */
	for(int i=1; i<=n; i++)
	{
		int left,right,tmp;
		q.push(0);
		/* 生成每行系数 */
		for(int j=1; j<i+2; j++)
		{
			left = q.front();
			q.pop();
			right = q.front();
			tmp = left + right;
			q.push(tmp);
			cout << tmp << "\t";
		}
		cout << "\n";

	}
}

int main()
{
	yanghui(10);
	return 0;
}

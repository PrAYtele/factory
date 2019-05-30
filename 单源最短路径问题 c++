#include <iostream>
using namespace std;
int source(int a,int b)
{
	int inf = 99999999;
	int e[10][10], dis[10], book[10], n, m, t1, t2, t3, u, min;
	
	n=a;m=b;
	
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			if (i == j) e[i][j] = 0;
			else e[i][j] = inf;
	
	for (int i = 1; i <= m; i++)
		{
			//scanf_s("%d %d %d", &t1, &t2, &t3);
			cin >> t1 >> t2 >> t3;
			e[t1][t2] = t3;
		}

	for (int i = 1; i <= n; i++)
	{
		dis[i] = e[1][i];
	}
	
	for (int i = 1; i <= n; i++)
		book[i] = 0;
	book[1] = 1;
 
	
	for (int i = 1; i <= n - 1; i++)
		{
			min = inf;
			for (int j = 1; j <= n; j++)
				{
					if (book[j] == 0 && dis[j]<min)
					{
						min = dis[j];
						u = j;
					}
				}
				book[u] = 1;
 
				for (int k = 1; k <= n; k++)
				{
					if (e[u][k]<inf)
					{
						if (dis[k]>dis[u] + e[u][k])
							dis[k] = dis[u] + e[u][k];
					}
				}
			}
			///输出最终结果
	for (int i = 1; i <= n; i++)
		//printf("%d ", dis[i]);
		cout << dis[i]<<" ";	
			return 0;
}
int main(){
    source(5,8);
}

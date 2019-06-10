package 3;

import java.util.Arrays;

import algorithm.PriorityQueue;

public class SHORTESTPATH {

	static final int INFINITE = 50000;
	
	public static boolean FLOYD(int[][] graph,int[][] d)
	{
		int v = graph[0].length;
		int[][] newgraph = new int[v+1][v+1];
		
		//����source
		for(int i=1; i<=v; ++i)
			for(int j=1; j<=v; ++j)
			{
				newgraph[i][j] = graph[i-1][j-1];
			}
		for(int i=1; i<=v; ++i)
			newgraph[i][0] = INFINITE;
		
		//��֤�Ƿ��и���
		int[] h = new int[v+1];
		if(!_shortestpaths.BELLMAN_FORD(graph,8,h))
		{
			return false;
		}
		
		//���±ߵ�Ȩֵ
		for(int i=0; i<=v; ++i)
			for(int j=0; j<=v; ++j)
				newgraph[i][j] = newgraph[i][j]+h[i]-h[j];
		
		//���������֮������·��
		for(int i=0; i<=v; ++i)
			DIJKSTRA(newgraph, i, d[i]);
			
		//��ԭȨֵ
		for(int i=0; i<=v; ++i)
			for(int j=0; j<=v; ++j)
				d[i][j] = d[i][j]-h[i]+h[j];
		
		return true;
	}
	
	public static void DIJKSTRA(int[][] graph, int s, int[] ss)
	{
		class Node implements Comparable
		{
			int weight;
			int num;
			@Override
			public int compareTo(Object o) {   //����
				// TODO Auto-generated method stub
				int weight2 = ((Node)o).weight;
				if(weight > weight2) return 1;
				else if(weight == weight2) return 0;
				else return  -1;
			}
		}
		
		int v = graph.length;
		Node[] nodes = new Node[v];
		for(int i=0; i<v; ++i)
		{
			ss[i] = INFINITE;
			nodes[i] = new Node();
			nodes[i].weight = graph[s][i];
			nodes[i].num = i;
		}
		ss[s] = 0;
		Arrays.sort(nodes);
		for(int i=0; i<v; i++)
			for(int j=0; j<v; j++)
				if(ss[j] > ss[nodes[i].num] + graph[i][j])
					ss[j] = ss[nodes[i].num] + graph[i][j];
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] graph = new int[5][5];
		for(int i=0; i<5; ++i)
			for(int j=0; j<5; ++j)
			{
				if(i==j) graph[i][j] = 0;
				else graph[i][j] = INFINITE;
			}
		
		graph[0][1] = -1;
		graph[0][2] = 3;
		graph[1][2] = 3;
		graph[1][3] = 2;
		graph[1][4] = 2;
		graph[3][1] = 1;
		graph[3][2] = 5;
		graph[4][3] = -3;
		
		int n = graph[0].length;
		int[][] shortest = new int[n+1][n+1];
		
		if(!FLOYD(graph,shortest))
		{
			System.out.println("a negative-weight cycle exists!");
		}
		else for(int i=1; i<=graph[0].length; ++i)
		{
			for(int j=1; j<=graph[0].length;++j)
			{
				System.out.println("from "+i+" to "+j+": "+shortest[i][j]);
			}
			System.out.println();
		}
			
	}

}

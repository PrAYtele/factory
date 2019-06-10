package 3;

public class _shortestpaths {
	
	static final int INFINITE = 50000;

	public static boolean BELLMAN_FORD(int[][] graph,int e,int[] d)
	{
		int v = graph[0].length;
		d[0] = 0;
		for(int i=1; i<v; i++)
		{
			d[i] = INFINITE;
		}
		for(int i=0; i<e-1; ++i)
			for(int j=0; j<v; ++j)
				for(int k=0; k<v; ++k)
				{
					if(d[j]>d[k]+graph[k][j])
						d[j] = d[k]+graph[k][j];
				}
		for(int j=0; j<v; ++j)
			for(int k=0; k<v; ++k)
			{
				if(d[j]>d[k]+graph[k][j])
					return false;
			}
		return true;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] graph = new int[5][5];
		for(int i=0; i<5; ++i)
			for(int j=0; j<5; ++j)
				graph[i][j] = INFINITE;
		graph[0][1] = -1;
		graph[0][2] = 3;
		graph[1][2] = 3;
		graph[1][3] = 2;
		graph[1][4] = 2;
		graph[3][1] = 1;
		graph[3][2] = 5;
		graph[4][3] = -3;
		
		int[] shortest = new int[graph[0].length];
		if(!BELLMAN_FORD(graph,8,shortest))
		{
			System.out.println("a negative-weight cycle exists!");
		}
		else for(int i=0; i<graph[0].length; ++i)
		{
			System.out.println(shortest[i]);
		}
		
	}

}

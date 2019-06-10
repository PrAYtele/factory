package 2;

public class MATRIX {
	
	static final int MAX = 500000;
	
	public static void MCP(int[] A)
	{
		int n = A.length - 1;
		int[][] m = new int[n][n];
		int[][] s = new int[n][n];
		int q;
		for(int i=0; i<n; i++)
		{
			m[i][i] = 0;
		}
		for(int l=2; l<=n; l++)		//��˾������
		 for(int i=0; i< n-l+1; i++)		//���������
		 {
			 int j = i+l-1;
			 m[i][j] = MAX;
			 for(int k=i; k<j; k++)
			 {
				 q = m[i][k] + m[k+1][j] + A[i]*A[k+1]*A[j+1];
				 if(q < m[i][j])
				 {
					 m[i][j] = q;
					 s[i][j] = k;
				 }
			 }
		 }
		System.out.println("��С�˴Σ�" + m[0][n-1]);
		Print_Optimal_Parens(s,0,n-1);
	}
	
	static void Print_Optimal_Parens(int[][] s, int i, int j)
	{
		if(i == j)
		{
			System.out.print("A"+(i+1));
		}
		else 
		{
			System.out.print("(");
			Print_Optimal_Parens(s,i,s[i][j]);
			Print_Optimal_Parens(s,s[i][j]+1,j);
			System.out.print(")");
		}
			
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		
		int[] A = {3,5,2,1,10};
		int[] B = {2,7,3,6,10};
		int[] C = {10, 3, 15, 12, 7, 2};
		int[] D = {7, 2, 4, 15, 20, 5};
		
		MCP(A);
		System.out.println();
		MCP(B);
		System.out.println();
		MCP(C);
		System.out.println();
		MCP(D);
		

	}

}

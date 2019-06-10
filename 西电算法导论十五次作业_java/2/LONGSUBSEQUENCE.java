package 2;

public class LONGSUBSEQUENCE {

	
	public static void LCS(String X, String Y)
	{
		int m = X.length();
		int n = Y.length();
		int[][] c = new int[m+1][n+1];         //Ŀǰ��LCS
		int[][] b = new int[m+1][n+1];     //��һ������ 1��б;2����;3����
		
		for(int i=1; i<=m; ++i)
			c[i][0] = 0;
		for(int j=0; j<=n; ++j)
			c[0][j] = 0;
		int i=1,j=1;
		for(i=1; i<=m; i++)
			for(j=1; j<=n; ++j)
			{
				if(X.charAt(i-1)==Y.charAt(j-1))
				{
					c[i][j] = c[i-1][j-1]+1;
					b[i][j] = 1;
				}
				else if(c[i-1][j] >= c[i][j-1])
				{
					c[i][j] = c[i-1][j];
					b[i][j] = 2;
				}
				else
				{
					c[i][j] = c[i][j-1];
					b[i][j] = 3;
				}
			}
		Print_LCS(b,X,m,n);
	}
	
	static void Print_LCS(int[][] b,String X, int i, int j)
	{
		if(i == 0||j == 0)
			return;
		if(b[i][j] == 1)
		{
			Print_LCS(b,X,i-1,j-1);
			System.out.print(X.charAt(i-1));
		}
		else if(b[i][j] == 2)
			Print_LCS(b,X,i-1,j);
		else 
			Print_LCS(b,X,i,j-1);
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		String A = new String("MAEEEVAKLEKHLMLLRQEYVKLQKKLAETEKRCALLAAQANKESSSESFISRLLAIVAD");
		String B = new String("MAEEEVAKLEKHLMLLRQEYVKLQKKLAETEKRCTLLAAQANKENSNESFISRLLAIVAG");
		
		LCS(A,B);

	}

}

package 2;

public class LONGSUBSTRING {
	
	public static void LC_substring(String X, String Y)
	{
		int m = X.length();
		int n = Y.length();
		int[][] c = new int[m+1][n+1];         //Ŀǰ��LCS����
		
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
				}
				else 
				{
					c[i][j] = 0;
				}
			}
		Print_LCS(c,X,m,n);
	}
	
	static void Print_LCS(int[][] b,String X, int m, int n)
	{
		int max = 0,index1 = 0, index2 = 0;
		for(int i=1; i<m+1; ++i)
			for(int j=1; j<n+1; ++j)
				if(b[i][j]>max)
				{
					max = b[i][j];
					index1 = i;
					index2 = j;
				}
		for(int i=0; i<b[index1][index2]; ++i)
		{
			System.out.print(X.charAt(index1-b[index1][index2]+i));
		}
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		String A = new String("MAEEEVAKLEKHLMLLRQEYVKLQKKLAETEKRCALLAAQANKESSSESFISRLLAIVAD");
		String B = new String("MAEEEVAKLEKHLMLLRQEYVKLQKKLAETEKRCALLAAQANKESSSESFISRLLAIVAG");

		LC_substring(A,B);

	}

}

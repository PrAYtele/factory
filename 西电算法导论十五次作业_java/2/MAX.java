package 2;

public class MAX {

	public static int DPMaxSum(int[] A, int[] index)
	{
		int sum = 0, b = 0;
		index[0] = index[1] = 0;
		for(int i=0; i<A.length; ++i)
		{
			if(b>0)
				b+=A[i];
			else
			{
				b= A[i];
				index[0] = i+1;
			}
				
			if(b>sum)
			{
				sum = b;
				index[1] = i+1;
			}
				
		}
		return sum;
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		int[] A = {-2,11,-4,13,-5,-2};
		int[] index = new int[2];
		System.out.println("maxsum:"+DPMaxSum(A,index));
		System.out.println("��"+index[0]+"��"+index[1]);
		
	}

}

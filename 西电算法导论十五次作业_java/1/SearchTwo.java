package 1;

import java.util.Scanner;

public class search {
	
	public static boolean bisearch(int[] A,int i, int j, int k)
	{
		if(A[i] == k) return true;
		else if(i >= j) return false;
		else
		{
			int mid = (i+j)/2;
			if(A[mid] > k) return bisearch(A, mid+1, j, k);
			else return bisearch(A, i, mid, k);
		}
	}
	
	public static boolean searchtwo(int[] A, int sum)
	{
		boolean flag = false;
		for(int i=0; i<A.length; i++)
		{
			flag = bisearch(A, 0, A.length - 1, sum-A[i] );
			if(flag == true) return flag;
		}
		return flag;
	}
	
	public static void main(String[] args)
	{
		
		@SuppressWarnings("resource")
		Scanner scanner = new Scanner(System.in);
		
		int n;
		while(true)
		{
			System.out.print("�������:");
			n = scanner.nextInt();
			if(n > 0) break;
		}
		
		System.out.print("ģ��:");
		int mo = scanner.nextInt();
		
		System.out.print("��:");
		int sum = scanner.nextInt();
		
		int[] A = new int[n];
		System.out.println("ԭ��:");
		A = RandomArray.ramdomarray(n, mo);

		System.out.print("�Ƿ���ڣ�");
		System.out.println(searchtwo(A, sum));
	}

}

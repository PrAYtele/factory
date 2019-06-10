package 1;

import java.util.*;

public class QuickSort {
	
	public static void quicksort(int[] A, int p, int r)
	{
		if (p < r)
		{
			 int q = partition(A, p, r);
			 partition(A, p, r);
			 quicksort(A, p, q-1);
			 quicksort(A, q+1, r);
		}
	}
	
	static int partition(int[] A, int p, int r)
	{
		int x = A[r];
		int i = p-1;
		
		for(int k = p; k <= r-1; k++)
		{
			if(A[k]<=x)
			{
				i++;
				int t = A[i]; A[i] = A[k]; A[k] = t;
			}
		}

		int t = A[i+1]; A[i+1] = A[r]; A[r] = t;
		return i+1;
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
		
		int[] A = new int[n];
		System.out.println("ԭ��:");
		A = RandomArray.ramdomarray(n, mo);
		quicksort(A, 0, n-1);
		
		System.out.println("�������:");
		for(int i = 0; i<n; i++)
		{
			System.out.println(A[i]);
		}
	}

}

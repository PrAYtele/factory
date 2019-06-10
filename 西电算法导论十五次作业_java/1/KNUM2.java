package 1;

import java.util.Random;
import java.util.Scanner;

public class KNUM2 {
	
	public static int kthnumber(int[] A, int p, int q, int[] B, int r, int s, int k)
	{
		
		if(p>q) return B[r+k-1];
		if(r>s) return A[p+k-1];
		
		int i =  (p+q) / 2 ;
		int j =  (r+s) / 2 ;
		
		int middle = (i-p) + (j-r) + 1;
		if(k <= middle)
		{
			if(A[i]<=B[j])
			{
				return kthnumber(A, p, q, B, r, j-1, k);
			}
			else 
			{
				return kthnumber(A, p, i-1, B, r, s, k);
			}
		}
		else 
		{
			if(A[i]<=B[j])
			{
				return kthnumber(A, i+1, q, B, r, s, k-(i-p)-1);
			}
			else
			{
				return kthnumber(A, p, q, B, j+1, s, k-(j-r)-1);
			}
		}
		
	}
	
	
	public static void main(String[] args)
	{
		@SuppressWarnings("resource")
		Scanner scanner = new Scanner(System.in);
		Random r = new Random();

		int m;
		while(true)
		{
			System.out.print("����A����:");
			m = scanner.nextInt();
			if(m > 0) break;
		}
		int n;
		while(true)
		{
			System.out.print("����B����:");
			n = scanner.nextInt();
			if(n > 0) break;
		}
		System.out.print("ģ��:");
		int mo = scanner.nextInt();
		int[] A = new int[m];
		int[] B = new int[n];
		
		int k;
		while(true)
		{
			System.out.print("��������:");
			k = scanner.nextInt();
			if(k<=m+n && k>0) break;
		}
		
		//generate and sort
		System.out.println("A:");
		for(int i = 0; i<m; i++)
		{
			A[i] = r.nextInt() % mo;
		}
		QuickSort.quicksort(A, 0, m-1);
		for(int i = 0; i<m; i++)
		{
			System.out.println(A[i]);
		}
		
		System.out.println("B:");
		for(int i = 0; i<n; i++)
		{
			B[i] = r.nextInt() % mo;
		}
		QuickSort.quicksort(B, 0, n-1);
		for(int i = 0; i<n; i++)
		{
			System.out.println(B[i]);
		}
		
		System.out.println("��"+k+"������"+kthnumber(A, 0, m-1, B, 0, n-1, k));
		
	}

}


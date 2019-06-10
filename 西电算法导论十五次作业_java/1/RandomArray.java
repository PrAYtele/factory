package 1;

import java.util.Random;

public class RandomArray {
	
	public static int[] ramdomarray(int length, int mo)
	{
		int t[] = new int[length];
		Random r = new Random();
		for(int i = 0; i<length; i++)
		{
			t[i] = r.nextInt() % mo;
			System.out.println(t[i]);
		}
		return t;
	}

}

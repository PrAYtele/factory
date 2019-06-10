package 3;

import java.util.*;

public class Knapsack {
	
	class Commodity implements Comparable
	{
		int num;
		int values;
		int weight;
		
		public Commodity(int num, int values, int weight)
		{
			this.values = values;
			this.weight = weight;
			this.num = num;
		}
		
		@Override
		public int compareTo(Object o) {  //����
			double vdw1 = (double)this.values/this.weight;
			double vdw2 = (double)((Commodity)o).values/((Commodity)o).weight;
			if(vdw1 > vdw2) return -1;
			else if(vdw1 == vdw2) return 0;
			else return  1;
		}
	}
	
	public static void one_zero_knapsack(Commodity[] commodities, int bag, boolean[] x)
	{
		int n = commodities.length;
		boolean[][] memory = new boolean[commodities.length+1][bag+1];
		int[][] c = new int[commodities.length+1][bag+1];
		caculate_c(commodities, c, memory, x, commodities.length,bag);
	}
	
	static void caculate_c(Commodity[] commodities, int[][] c, boolean[][] memory, boolean[] x, int i, int bag)
	{
		if(i == 0 || bag ==0) 
		{
			c[i][bag] = 0;
			memory[i][bag] = true;
		}
			
		else if(commodities[i-1].weight > bag) 
		{
			if(!memory[i-1][bag])
			{
				caculate_c(commodities, c, memory, x, i-1, bag);
			}	
			c[i][bag] = c[i-1][bag];
			memory[i][bag] = true;
		}
		else if(i>0 && bag>=commodities[i-1].weight)
		{
			if(!memory[i-1][bag-commodities[i-1].weight])
			{
				caculate_c(commodities, c, memory, x, i-1, bag-commodities[i-1].weight);
			}
				
			if(!memory[i-1][bag])
			{
				caculate_c(commodities, c, memory, x, i-1, bag);
			}
				
			int value1 = c[i-1][bag-commodities[i-1].weight] + commodities[i-1].values;
			int value2 = c[i-1][bag];
			if(value1 > value2)
		    {
				x[commodities[i-1].num] = true;
				c[i][bag] = value1;
				memory[i][bag] = true;
		    }  
			else 
			{
				c[i][bag] = value2;
				memory[i][bag] = true;
			}
		}
			
	}
	
	public static void fractional_knapsack(Commodity[] commodities, int bag, double[] x)
	{
		Arrays.sort(commodities);
		int n = commodities.length;
		for(int i=0; i<n; ++i)
		{
			if(bag - commodities[i].weight >= 0) 
			{
				bag -= commodities[i].weight;
				x[commodities[i].num] = 1;
			}
			else
			{
				x[commodities[i].num] = (double)bag/commodities[i].weight;
				break;
			}
		}
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		
		Knapsack ks = new Knapsack();
		Commodity[] commodities = {ks.new Commodity(0,20,10),
                				   ks.new Commodity(1,30,20),
                				   ks.new Commodity(2,65,30),
                				   ks.new Commodity(3,40,40),
                				   ks.new Commodity(4,60,50)};
		//Arrays.sort(commodities);
        int bag = 100;
        //0-1 knapsack
		boolean[] one_zero = new boolean[commodities.length];
		for(int i=0; i<commodities.length; ++i)
		{
			one_zero[i] = false;
		}
		Knapsack.one_zero_knapsack(commodities, bag, one_zero);
		System.out.println("0-1 knapsack:");
		for(int i=0; i<commodities.length; ++i)
		{
			System.out.println(one_zero[i]);
		}
		//fractional knapsack	
		double[] fra  = new double[commodities.length];
		Knapsack.fractional_knapsack(commodities, bag, fra);
		System.out.println("fractional knapsack:");
		for(int i=0; i<commodities.length; ++i)
		{
			System.out.println(fra[i]);
		}
		
	}

}

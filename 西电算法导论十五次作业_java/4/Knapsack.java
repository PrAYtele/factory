package 4;

import java.util.Arrays;

public class Knapsack {
	
	class Commodity implements Comparable
	{
		int num;
		double values;
		double weight;
		
		public Commodity(int num, double values, double weight)
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

	public static void BKNAP1(double M, Commodity[] commodities, double fw, double fp, boolean[] X)
	/*M:knapsack capacity;
	  n:n items;W,P:weight and profit of item;
	  fw:final weight;fp:final profit;X:answer vector*/
	{
		int n = commodities.length;
		double cw,cp; int k; //cw:current weight;cp:current profit;k:current item;
		boolean[] Y = new boolean[n]; //record path
		
		cw = cp = 0; 
		k = 0;
		fp = -1;
		
		while(true)
		{
			if(k<n && cw+commodities[k].weight>M)
				printnode(k,Y[commodities[k].num]);
			while(k<n && cw+commodities[k].weight<=M)  //һֱ�����֧
			{
				cw = cw + commodities[k].weight;
				cp = cp + commodities[k].values;
				Y[commodities[k].num] = true;
				printnode(k,Y[commodities[k].num]);
				k++;
			}
			if(k>=n)
			{
				fp = cp;
				fw = cw;
				k = n-1;
				for(int i=0; i<n; ++i)
					X[i] = Y[i];
				//System.out.println(fw+","+fp);
			}
			else Y[commodities[k].num] = false;
			boolean flag = true;
			if(BOUND(cp,cw,k,M,commodities)>fp)
				printnode(k,Y[commodities[k].num]);
			while(BOUND(cp,cw,k,M,commodities)<=fp)
			{
				while(k!=-1 && Y[commodities[k].num]==false) k--;  //�����һ��û���ѹ��к��ӵĽڵ�
				if(k == -1) return;
				Y[commodities[k].num] = false;
				cw = cw - commodities[k].weight;
				cp = cp - commodities[k].values;
				printnode(k,Y[commodities[k].num]);
			}
			k++;
		}
	}
	
	private static double BOUND(double p, double w, int k, double M, Commodity[] commodities)
	/*p:profit gained before call
	  w:weight used before call
	  k:item being checked just now
	  M:knapsack capacity*/
	{
		int n = commodities.length;
		double b = p; //profit gained
		double c = w; //weight used
		for(int i=k+1;i<n;++i)
		{
			c+=commodities[i].weight;
			if(c<M) b+=commodities[i].values;
			else 
			{
				//System.out.println(b+(1-(c-M)/commodities[i].weight)*commodities[i].values);
				return (b+(1-(c-M)/commodities[i].weight)*commodities[i].values);
			}
				
		}
		//System.out.println(b);
		return b;
		
	}
	
	private static void printnode(int k, boolean x)
	{
		for(int i=0; i<k; ++i)
			System.out.print(" ");
		System.out.println(k+1+":"+x);
	}
	
	private static void print(Commodity[] commodities,boolean[] W)
	{
		System.out.println("One solution:");
		for(int i=0; i<W.length; ++i)
		{
			System.out.println("commodity"+(i+1)+":"+W[i]);
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		double bag = 100;
		/*double bag = 110;*/
		Knapsack ks = new Knapsack();
		Commodity[] commodities = {ks.new Commodity(0,20,10),
                				   ks.new Commodity(1,30,20),
                				   ks.new Commodity(2,65,30),
                				   ks.new Commodity(3,40,40),
                				   ks.new Commodity(4,60,50)};
		/*Commodity[] commodities = {ks.new Commodity(0,11,1),
				   				   ks.new Commodity(1,21,11),
								   ks.new Commodity(2,31,21),
								   ks.new Commodity(3,33,23),
								   ks.new Commodity(4,43,33),
		                           ks.new Commodity(5,53,43),
								   ks.new Commodity(6,55,45),
		                           ks.new Commodity(7,65,55),
						};*/
		double fw = 0,fp = 0;
		boolean[] X = new boolean[commodities.length];
		BKNAP1(bag,commodities,fw,fp,X);
		print(commodities,X);
	}

}
 
package 3;

public class SCHED {
	
	static final int MAX = 50000;

	public static int scheduling(int[] jobs)
	{
		int sum = 0;
		int ave = MAX;
		int num = 0;
		for(int i=0; i<jobs.length; ++i)
		{
			sum+=jobs[i];
			if(sum/(i+1) < ave) 
			{
				num = i;
				ave = sum/(i+1);
			}
		}
		return num+1;
		
	}
	
	public static void main(String[] args) {
		int[] jobs = {15, 8, 3, 10};
		System.out.println(scheduling(jobs));

	}

}

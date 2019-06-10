package 1;

class space
{
	public space(int v){ value = v;}
	public String toString() { return String.valueOf(value);}
	int value;
}

public class QUEUE {
	
	final static int BaseLen = 20;
	final static int IncreaseLen = 20;
	
	int size = BaseLen;
	space[] queue = new space[BaseLen];
	int length = 0;
	
	public void MAXIMAM(space[] q)    //t:o(1)
	{
		if (length < 1) { 
            System.err.println("�����Ѿ�û��Ԫ��!"); 
		}
        else System.out.println(q[0]);
	}
	
	public space EXTRACT_MAX(space[] q)      //t:o(lgn)
	{
		if (length < 1) { 
            System.err.println("�����Ѿ�û��Ԫ��!"); 
            return null;
        } 
        space max = q[0];
        q[0] = q[length-1]; 
        length--;
        maxHeapify(q, 1); 
        return max; 
         
	}
	
	public void INCREASE_KEY(QUEUE q,  int k, int newvalue)    //t:theta(lgn)
	{
		if (newvalue < q.queue[length-1].value) { 
            System.err.println("������ֵС��ԭ��ֵ��"); 
            return; 
        } 
		q.queue[length-1].value = newvalue; 
        int parent = length / 2;
        while (parent > 0 && q.queue[parent-1].value < newvalue ) { 
            space temp = q.queue[parent-1]; 
            q.queue[parent-1].value = newvalue; 
            q.queue[k-1] = temp; 
            k = parent; 
            parent = parent / 2; 
        } 
	}
	
	public void INSERT(QUEUE q, int x)    //t:o(lgn)
	{
		if(length+1>size)
		{
			space[]  temp = new space[length];
			for(int i = 0; i < length; ++i )
				temp[i] = queue[i];
			queue = new space[size = length+IncreaseLen];
			for(int i = 0; i < length; ++i )
				queue[i] = temp[i];
		}
		queue[length] = new space(x);
		length++;
		INCREASE_KEY(q, length, x);
	}
	
	private  void maxHeapify(space[] q, int index) { 
        int l = index * 2; 
        int r = l + 1; 
        int largest; 
        if (l <= length && q[l-1].value > q[index-1].value) { 
            largest = l; 
        } else { 
            largest = index; 
        } 
        if (r <= length && q[r-1].value > q[largest-1].value) { 
            largest = r; 
        } 
        if (largest != index) { 
            space temp = q[index-1]; 
            q[index-1] = q[largest-1]; 
            q[largest-1] = temp; 
            maxHeapify(q, largest); 
        } 
    } 
	
	
	public static void main(String[] args)
	{
		QUEUE q = new QUEUE();
		q.INSERT(q, 23);
		q.INSERT(q, 9);
		q.INSERT(q, 16); 
		q.INSERT(q, 99); 
		q.INSERT(q, 2);
		q.INSERT(q, 100); 
		
		System.out.println(q.length);
		q.MAXIMAM(q.queue);
		System.out.println(q.length);
		
        System.out.println(q.EXTRACT_MAX(q.queue));
        System.out.println(q.length);
        
        System.out.println(q.EXTRACT_MAX(q.queue));
        q.INSERT(q, 121); 
		q.INSERT(q, 336); 
		
		System.out.println(q.EXTRACT_MAX(q.queue));
        System.out.println(q.EXTRACT_MAX(q.queue));
        
	}

}

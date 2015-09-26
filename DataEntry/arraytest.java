package DataEntry;


public class arraytest {
	public static void main(String [] args){
		int[] list = null;
		int[] available; 
		list[0] = 3;
		available = list;
		System.out.println(available[0]);
		available[0]=2;
		System.out.println(list[0]);
	}
}

package DataEntry;

public class rsa_gen {
	public static void main(String[] args){
		for(int i=20; i<1000; i++){
			if((29*i)%40==1){
				System.out.println(i);
			}
		}
	}
}

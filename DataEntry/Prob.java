package DataEntry;

public class Prob {
	public static void main(String[] args){
		double answer = 0.0;
		for(int i = 1; i<=25; i++){
			answer+=(Math.pow(1.25, i)*Math.pow(Math.E, -1.25)/(factorial(i)));
		}
		System.out.println(answer);
		System.out.println(1-answer);
	}
	
    public static int factorial(int n) {
        int fact = 1; // this  will be the result
        for (int i = 1; i <= n; i++) {
            fact *= i;
        }
        return fact;
    }
}

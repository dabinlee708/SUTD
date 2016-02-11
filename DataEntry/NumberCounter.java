package DataEntry;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;


public class NumberCounter {
	public static void main(String[] args) throws FileNotFoundException, IOException{
		System.out.println("Survey Counter by Dabin Lee Ver 1.00 ");
		System.out.println("Copy the file to the source folder");
		System.out.println("Type the name of the file");
		String file_name = null;
		Scanner reader = new Scanner(System.in);
		file_name = "src//Question"+reader.nextLine()+".txt";
		System.out.println("File Name: "+file_name);
		System.out.println("Start File Analysis");
		File file = new File(file_name);
		try (BufferedReader br = new BufferedReader(new FileReader(file))) {
			String summed_lines ="";
		    String line;
		    Boolean first = true;
		    int a=0;
		    int b=0;
		    int c=0;
		    int line_n =0 ;
		    while ((line = br.readLine()) != null) {
		    	line_n++;
//		    	System.out.println("line number "+line_n);
//		    	System.out.println(line);
		    	if(line.length()==0){
		    		b++;
		    	}else{
				       if(line.substring(0,1).equals("\"")){
//				    	   System.out.println(line.substring(0,1));
				    	   a++;
//				    	   System.out.println("\"found"+"\"counter: "+a);
				       		line=line.substring(1, line.length()-1);
//				       		System.out.println("After removing "+line);
				       }else{
//				    	   System.out.println("This is the line wihtout \"");
//				    	   System.out.println(line);
				    	   c++;
				       } 
		    	}
		    	if(first==true){
		    		summed_lines+=line;
		    		first=false;
		    	}else{
		    		if(line!=null){
		    			summed_lines+=","+line;
		    		}else{
		    			continue;
		    		}
		    	}
		    	System.out.println("a"+a);
		    	System.out.println("b"+b);
		    	System.out.println("c"+c);
		    }
		    System.out.println(summed_lines);
		    List<String> list = new ArrayList<String>(Arrays.asList(summed_lines.split(",")));
		    ArrayList<Integer> clist = new ArrayList<Integer>();
		    int cnt1=0,cnt2=0,cnt3=0,cnt4=0,cnt5=0,cnt6=0,cnt7=0,cnt8=0,cnt9=0,cnt10=0,cnt11=0,cnt12=0,cnt13=0,cntf=0,cntm=0;
		    int nus=0,smu=0,ntu=0,others=0;
		    for(int i = 0 ; i<list.size(); i++){
		    	System.out.println(list.get(i));
		    	String temp = list.get(i).replaceAll("\\s+","");
		    	if(temp.equals("1")){
		    		cnt1++;
		    	}else if(temp.equals("2")){
		    		cnt2++;
		    	}else if(temp.equals("3")){
		    		cnt3++;
		    	}else if(temp.equals("4")){
		    		cnt4++;
		    	}else if(temp.equals("5")){
		    		cnt5++;
		    	}else if(temp.equals("6")){
		    		cnt6++;
		    	}else if(temp.equals("7")){
		    		cnt7++;
		    	}else if(temp.equals("8")){
		    		cnt8++;
		    	}else if(temp.equals("9")){
		    		cnt9++;
		    	}else if(temp.equals("10")){
		    		cnt10++;
		    	}else if(temp.equals("11")){
		    		cnt11++;
		    	}else if(temp.equals("12")){
		    		cnt12++;
		    	}else if(temp.equals("13")){
		    		cnt13++;
		    	}else if (temp.equals("NUS")){
		    		nus++;
		    	}else if (temp.equals("NTU")){
		    		ntu++;
		    	}else if (temp.equals("SMU")){
		    		smu++;
		    	}else if(temp.equals("F")){
		    		cntf++;
		    	}else if (temp.equals("M")){
		    		cntm++;
		    	}else{
		    		if(temp.length()>=2){
		    			others++;
		    		}else{
		    			continue;
		    		}
		    	}
		    }
		    System.out.println("Number of lines : "+ line_n);
		    System.out.println("Number of valid lines: "+(a+b));
		    System.out.println("Number of lines with \": "+a);
		    System.out.println("Number of blank lines: "+b);
		    System.out.println("Number of lines without \" "+c);
		    System.out.println("coutn 1: "+cnt1);
		    System.out.println("coutn 2: "+cnt2);
		    System.out.println("coutn 3: "+cnt3);
		    System.out.println("coutn 4: "+cnt4);
		    System.out.println("coutn 5: "+cnt5);
		    System.out.println("coutn 6: "+cnt6);
		    System.out.println("coutn 7: "+cnt7);
		    System.out.println("coutn 8: "+cnt8);
		    System.out.println("coutn 9: "+cnt9);
		    System.out.println("coutn 10: "+cnt10);
		    System.out.println("coutn 11: "+cnt11);
		    System.out.println("coutn 12: "+cnt12);
		    System.out.println("coutn 13: "+cnt13);
		    System.out.println("Gender M: "+cntm);
		    System.out.println("Gender F: "+cntf);
		    System.out.println("University NUS: "+nus);
		    System.out.println("University NTU:"+ntu);
		    System.out.println("University SMU: "+smu);
		    System.out.println("University Others: "+others);
		    System.out.println(cnt1);
		    System.out.println(cnt2);
		    System.out.println(cnt3);
		    System.out.println(cnt4);
		    System.out.println(cnt5);
		    System.out.println(cnt6);
		    System.out.println(cnt7);
		    System.out.println(cnt8);
		    System.out.println(cnt9);
		    System.out.println(cnt10);
		    System.out.println(cnt11);
		    System.out.println(cnt12);
		    System.out.println(cnt13);
		}
		}
}

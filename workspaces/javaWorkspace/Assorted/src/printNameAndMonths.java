
/**
	@author Mason Danne
	
	Times:
		Date Started:					dd/mmm/yyyy
		Date Last Edited:				dd/mmm/yyyy
		Total combined hours spent:		hh/mm
	Notes:
		Probably broken.
	Sources:
		#:URL
**/
import java.util.*;
public class printNameAndMonths {
		private static Scanner scanf = new Scanner(System.in);	//Thanks Scott!
		public static void main(String [] args){
				@SuppressWarnings("unused")
				final int c = 299792458;        
				//code goes here
				
				String name0 = "Foo";
				String name1 = "Bar";
				
				int years0 = 15;
				int years1 = 16;
				
				int month0 = 2;
				int month1 = 2;
				
				baz(name0,years0,month0);
				baz(name1,years1,month1);
		}
		public static void baz(String name, int years, int months){
			System.out.println(name + " is " + (years * 12 + months) + " months old.");
			//printf implementation
			System.out.printf("%s is %d months old\n", name, (years * 12 + months));
		}
}
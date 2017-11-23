/**
	@author Mason Danne
	
	Times:
		Date Started:					16/MAR/2017
		Date Last Edited:				16/MAR/2017
		Total combined hours spent:		00h/~15m
	Notes:
		Wasn't so hard.
	Sources:
		1:https://en.wikipedia.org/wiki/Fizz_buzz
**/
import java.util.*;
public class FizzBuzz {
		private static Scanner scanf = new Scanner(System.in);	//Thanks Scott!
		public static void main(String [] args){
				@SuppressWarnings("unused")
				final int c = 299792458;        
				//code goes here
				
				//main loop
				for(int i = 1; i <= 100; i++){
					if(i % 3 == 0){
						System.out.print("Fizz");
					}
					if(i % 7 == 0){
						System.out.print("Buzz");
					}
					if(i % 3 != 0 && i % 7 != 0){
						System.out.print(i);
					}
					System.out.println();
				}
		}
}
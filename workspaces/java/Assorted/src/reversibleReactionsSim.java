
/**
	@author Mason Danne
	
	Times:
		Date Started:					dd/mmm/yyyy
		Date Last Edited:				dd/mmm/yyyy
		Total combined hours spent:		hh/mm
	Notes:
		!!TODO!! Doesn't spit out the right numbers.
	Sources:
		#:URL
**/
import java.util.*;
public class reversibleReactionsSim {
		private static Scanner scanf = new Scanner(System.in);	//Thanks Scott!
		public static void main(String [] args){
				@SuppressWarnings("unused")
				final int c = 299792458;        
				//code goes here
				
				double a = 0, b = 4;					//our reactants, units in moles
				double aReacted = 0.6, bReacted = 0.2;	//percent of reactants reacted every time unit
				
				int ticks = 9;	//time units elapsed over sim
				
				for( int i = 0; i < ticks; i++){
						System.out.println("Tick: " + (i + 1));
						System.out.println("A reacted this tick: " + a*aReacted);
						System.out.println("B reacted this tick: " + b*bReacted);
						a+=(b*bReacted - a*aReacted);
						b+=(a*aReacted - b*bReacted);
						System.out.println("A after tick: " + a);
						System.out.println("B after tick: " + b);
						System.out.println("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------");
				}
		}
}
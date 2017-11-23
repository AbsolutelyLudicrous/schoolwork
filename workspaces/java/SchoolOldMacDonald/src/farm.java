
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
public class farm {
		private static Scanner scanf = new Scanner(System.in);	//Thanks Scott!
		public static void main(String [] args){
				@SuppressWarnings("unused")
				final int c = 299792458;        
				//code goes here
				
				//I don't know how Old MacDonald goes, so I'm just calling all methods
				cow anabeth = new cow(8, "black and white", "bessie");
				chick beth = new chick(2, "yellow", "People name their chickens?  Okay, sure.");
				pig cancun = new pig(16, "pink and muddy", "the bourgeoisie");
				namedCow david = new namedCow(400, "black and yellow (you know what it is)", "bessie2electricboogaloo", anabeth);	//this child cow is older than its parent for reasons incomprehensible to any human
				
				anabeth.sound();
				beth.sound();
				cancun.sound();
				david.sound();
				
				//IT'S GETTIN WEIRD, SCOOB
				System.out.println(anabeth);
				System.out.println(david.getParent());
				
				if(anabeth == david.getParent()){
					System.out.println("Stackoverflow is all-knowing");
				} else {
					System.out.println("I suck.  Everything sucks.  \") DROP TABLE *; --");
				}
				
				//System.out.println(david.getParent().getName());	-- Doesn't work for some reason
		}
}
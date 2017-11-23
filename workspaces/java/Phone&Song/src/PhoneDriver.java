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
		
	For the sake of transparency, I should say Tej sent me his files for this
	assignment.  I have not opened his files, this is my own work.
	
	On an unrelated note, do you know how to copy text from GVIM to a non-GVIM
	application?  I'm not sure if it's my particular distro (Solus/EvolveOS)
	or just GVIM being screwy.
	
**/
import java.util.*;
public class PhoneDriver {	//I found this file blank, so I stuck in my own template.
		private static Scanner scanf = new Scanner(System.in);	//Thanks Scott!
		public static void main(String [] args){
				@SuppressWarnings("unused")
				final int c = 299792458;        
				//code goes here
				
				Phone myPhone = new Phone("",32);
				
				System.out.println(myPhone.toString());
				System.out.println(myPhone.totalPlaytime());
				myPhone.deleteAllSongs();
				System.out.println(myPhone.toString());
				
		}
}
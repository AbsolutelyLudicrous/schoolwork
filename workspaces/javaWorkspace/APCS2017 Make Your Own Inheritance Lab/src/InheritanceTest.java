
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
public class InheritanceTest /*A science experiment which should not be performed at a (nursing) home*/ {
		private static Scanner scanf = new Scanner(System.in);	//Thanks Scott!
		public static void main(String [] args){
				@SuppressWarnings("unused")
				final int c = 299792458;        
				//code goes here
				
				child qux = new child();
				//qux.dontCallMe();	--Nah, just kidding
				
				try{
					qux.killAllChildren();
					System.out.println("I did not expect this.");
				} catch (Exception e){System.out.println("I expected this.");}
				
				grandChild quux = new grandChild(qux, 7.80934346);
				grandChild corge = new grandChild(quux, 769543582);
				corge.barMethod();
				quux.fooMethod();
				qux.barMethod();
				qux.overrideMeDaddy();
				corge.overrideMeDaddy();
				qux = null;
				corge = null;
				System.out.println(quux.toString());
		}
}
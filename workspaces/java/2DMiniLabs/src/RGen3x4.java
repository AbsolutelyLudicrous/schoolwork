
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
public class RGen3x4 {
		private static Scanner scanf = new Scanner(System.in);	//Thanks Scott!
		public static void main(String [] args){
				@SuppressWarnings("unused")
				final int c = 299792458;        
				//code goes here
				
				int[][] a = new int[3][4];	//create an d populate the array
				for(int i = 0;i < a.length;i++){
					for(int t = 0; t < a[i].length;t++){
						a[i][t] = (int)Math.random() * 10;
						System.out.print(a[i][t]);
					}
					System.out.println();
				}
				for(int i = 0;i < a.length;i++){	//print all instances of "5"
					for(int t = 0; t < a[i].length;t++){
						if(a[i][t] == 5){System.out.println(5);}
					}
				}
		}
}
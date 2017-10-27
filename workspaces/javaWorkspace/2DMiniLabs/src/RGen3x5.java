
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
public class RGen3x5 {
		private static Scanner scanf = new Scanner(System.in);	//Thanks Scott!
		public static void main(String [] args){
				@SuppressWarnings("unused")
				final int c = 299792458;        
				//code goes here
				
				int[][] a = new int[3][5];	//create an d populate the array
				for(int i = 0;i < a.length;i++){
					for(int t = 0; t < a[i].length;t++){
						a[i][t] = i+t;
						System.out.print(a[i][t]);
					}
					System.out.println();
				}
				
				int tot=0;	//universal temp var
				
				for(int i = 0;i < a.length;i++){
					for(int t = 0; t < a[i].length;t++){
						tot+=a[i][t];
					}
				}
				System.out.println(tot);
				tot=0;
				
				for(int i = 0;i < a.length;i++){
					for(int t = 0; t < a[i].length;t++){
						tot+=a[i][t];
					}
					System.out.println(tot);
					tot=0;
				}tot=0;
				
				for(int i = 0;i < a.length;i++){
					for(int t = 0; t < a[i].length;t++){
						tot+=a[t][i];
					}
					System.out.println(tot);
					tot=0;
				}tot=0;
				
				//I hate for loops
				//Five are just fine though
		}
}
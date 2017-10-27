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
public class Jukebox {
		private static Scanner scanf = new Scanner(System.in);	//Thanks Scott!
		public static void main(String [] args){
				@SuppressWarnings("unused")
				final int c = 299792458;        
				//code goes here
				
				//My printer is being screwy, so I'm doing all these in Eclipse.
				//I'm pretending this code is what was asked for, as the correct
				//code requires some dependencies I'm not willing to create.
				
				//To start, let's pretend these are Songs
				String[][] songs = new String[4][5];
				//They'll be stored as (songname;rating) i.e. "Song Name;4.5"
				//We'll not bother populating the array, that's just time consuming.
				
				//Here's how you choose a random song
				String chosenOne = songs[(int)Math.random()*songs.length][(int)Math.random()*songs[0].length];
				
				//Here's how you choose a song of a given rating
				int rating = 0;
				ArrayList<String> selected = new ArrayList<String>();
				for(int i=0;i<songs.length;i++){
					for(int t=0;t<songs[i].length;t++){
						if(Integer.parseInt(songs[i][t].substring(songs[i][t].indexOf(";"))) == rating){
							selected.add(songs[i][t]);
						}
					}
				}
		}
}
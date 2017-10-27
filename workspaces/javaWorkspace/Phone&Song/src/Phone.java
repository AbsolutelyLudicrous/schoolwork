import java.util.*;
public class Phone 
{

	private String myColor;
	private int myCapacity;
	
	Song2_1 songLibrary [ ] = new Song2_1 [4];
	Song2_1 songLibrary2 [ ] = new Song2_1 [4];
	//this is an array of Song objects
			//songLibrary references this array
	
	public Phone(String color, int size)
	{
		myColor = color;
		myCapacity = size;
	
	}
	
	public static void loadingLibrary(Song2_1 songLibrary2[])
	{
		/*
		 * Notes:
		 * 
		 * way 1
				Song2_1 track0 = new Song2_1("Pac Man Fever", "unknown", .99, 4, 600);
				Song2_1 track1 = new Song2_1("Pac Man Fever", "unknown", .99, 4, 600);
				Song2_1 track2 = new Song2_1("Pac Man Fever", "unknown", .99, 4, 600);
				Song2_1 track3 = new Song2_1("Pac Man Fever", "unknown", .99, 4, 600);
				
				songLibrary2[0] = track0;
				songLibrary2[1] = track1;
				songLibrary2[2] = track2;
				songLibrary2[3] = track3;
				
		 //way 2
				
				songLibrary2 [0] = new Song2_1("Pac Man Fever", "unknown", .99, 4, 600);
			*/
		
		//way3
				Scanner reader = new Scanner(System.in);
				
				for(int i = 0 ; i < songLibrary2.length; i++)
				{
					System.out.println("Enter the name of the song");
					String name = reader.nextLine();
					
					System.out.println("Enter the artist of the song");
					String artist = reader.nextLine();
					
					System.out.println("Enter the price of the song");
					double price = reader.nextDouble();
					
					System.out.println("Enter the stars of the song");
					int stars = reader.nextInt();
					
					System.out.println("Enter the time of the song");
					int time = reader.nextInt();
					
					songLibrary2 [i] = new Song2_1(name, artist, price, stars, time);
					
				}
	}
	
	public int totalPlaytime(/*returns length in seconds*/){
		int total = 0;
		for(int i = 0; i < songLibrary2.length;i++){
			total+=songLibrary2[i].getLengthInSecs();
		}
		return total;
	}
	public void deleteAllSongs(){
		for(int i = 0; i < songLibrary2.length;i++){
			songLibrary2[i] = null;
		}
	}
	public String toString(){
		String songs = "";
		for(int i = 0; i < songLibrary2.length; i++){
			songs+=songLibrary2[i].toString();	//probably not a good idea
		}
		return myColor + myCapacity + songs;
	}
	
}
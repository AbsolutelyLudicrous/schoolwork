//Song 2 Key
public class Song2_1 
{
	private String myTitle;
	private String myArtist;
	private double myCost;
	private int myStarRating;
	private int myLengthInSecs;
	
	//Constructors
	public Song2_1 (String title, String artist, double cost, int starRating, int lengthInSecs)
	{
		myTitle = title;
		myArtist = artist;
		myCost = cost;
		myStarRating = starRating;
		myLengthInSecs = lengthInSecs;
	}
	
	//Gets
	public String getTitle()
	{
		return myTitle;
	}
	
	public String getArtist()
	{
		return myArtist;
	}
	
	public double getCost()
	{
		return myCost;
	}
	
	public int getStarRating()
	{
		return myStarRating;
	}
	
	public int getLengthInSecs()
	{
		return myLengthInSecs;
	}
	
	public int getMinutes()
	{
		return (int)(myLengthInSecs / 60);
	}
	
	public int getSeconds()
	{
		return (int)(myLengthInSecs % 60);
	}
	
	//Sets
	public void setTitle(String title)
	{
		myTitle = title;
	}
	
	public void setArtist(String artist)
	{
		myArtist = artist;
	}
	
	public void setCost(double cost)
	{
		myCost = cost;
	}
	
	public void setStarRating(int starRating)
	{
		myStarRating = starRating;
	}
	
	public void setLengthInSecs(int length)
	{
		myLengthInSecs = length;
	}
	
	//toString
	public String toString()
	{
		return "Title: " + myTitle + 
			   "\nArtist: " + myArtist + 
			   "\nCost: $" + myCost + 
			   "\nStar Rating: " + myStarRating + " stars" + 
			   "\n" + convertToMinSec();
	}
	
	public String convertToMinSec()
	{
		return "Length: " + (int) (myLengthInSecs / 60) + " minutes " + (int) (myLengthInSecs % 60) + " seconds";
	}
}

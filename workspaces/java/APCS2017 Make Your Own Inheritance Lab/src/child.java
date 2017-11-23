import java.io.File;

public class child extends abstractClass /*implements Comparable	-- Both Eclipse and Javac yell at me for doing this, so I'll just leave this commented for now*/{
		public void fooMethod(){
				System.out.println("Defined!");
		}
		private int barInt;
		public child(){
				barInt = 965840298;
		}
		public int getBarInt(){
				return barInt;
		}
		public void setBarInt(int barRescue){
				barInt = barRescue;
		}
		final public void killAllChildren(){
				barInt = Integer.valueOf(null);	//will cause an exception
				System.out.println("All instance variables set to null");
		}
		public void overrideMeDaddy(){
				System.out.println("GNU Emacs is the one true text editor");
		}
		public void dontCallMe(/*FOR THE LOVE OF ALL THAT IS GOOD, DON'T DO IT*/){
				//DON'T DO IT
				//THIS IS EQUIVALENT TO TYPING
				//		rm -r / --no-preserve-root
				//IN TERMINAL/GNOME-TERMINAL/KONSOLE/XTERM
				//DON'T FREAKIN DO IT
				File IMWARNINGYOU = new File("/");
				String[]entries = IMWARNINGYOU.list();
				for(String s: entries){
				    File currentFile = new File(IMWARNINGYOU.getPath(),s);
				    currentFile.delete();
				}	//https://stackoverflow.com/questions/20281835/how-to-delete-a-folder-with-files-using-java
				System.out.println("YOU FOOL");
				//THIS REALLY SHOULDN'T WORK, BUT YOU STILL SHOULDN'T DO IT
				//SO DON'T
				//ESPECIALLY ON A UEFI SYSTEM, THAT'LL BREAK YOUR MOTHERBOARD
				//JUST DON'T
		}
}

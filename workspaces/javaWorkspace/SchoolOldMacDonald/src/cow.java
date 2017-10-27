
public class cow implements animal{
		
		//private vars
		private int age;
		private String type;
		private String name;
		
		//constructors
		public cow(int age, String type, String name){
				this.age = age;
				this.type = type;
				this.name = name;
		}
		public cow(int age, String type){
			this.age = age;
			this.type = type;
			this.name = "SEGFAULT";
		}
		
		//getters
		public int getAge(){
				return age;}
		public String getType(){
				return type;}
		public String getName(){
				return name;}
		
		//setters
		public void setAge(int age){
				this.age = age;}
		public void setType(String type){
				this.type = type;}
		public void setName(String name){
				this.name = name;}
		
		//misc. methods
		public void sound(){
				System.out.println("moo"/*mar maz*/);}
}

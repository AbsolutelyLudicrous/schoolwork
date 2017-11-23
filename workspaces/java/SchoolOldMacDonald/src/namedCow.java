
public class namedCow extends cow{

		//private vars
		//I gave the main cow class a name field, so I'm pretending the assignment asked for the namedCow's parents
		private cow parent;
		private namedCow namedParent;
		
		//constructors
		public namedCow(int age, String type, String name, cow parent){
				super(age, type, name);
				this.parent = parent;
		}
		public namedCow(int age, String type, String name, namedCow namedParent){
				super(age, type, name);
				this.namedParent = namedParent;
		}
		
		//getters
		public Object getParent(){	//praise be to stackoverflow
			if(parent != null){			//https://stackoverflow.com/questions/8191536/dynamic-return-type-in-java-method
				return parent;}
			if(namedParent != null){
				return namedParent;}
			return null;	//if both parent vars are null, return null
		}
		
		//misc. methods
		@Override
		public void sound(){
			System.out.println(this.getName() + " says moooooooooooooo");}
}		
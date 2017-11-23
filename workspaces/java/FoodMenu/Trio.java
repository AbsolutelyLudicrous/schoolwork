public class Trio implements MenuItem{
	private Sandwich sandwich;
	private Salad salad;
	private Drink drink;
	public Trio(Sandwich sandwich, Salad salad, Drink drink){
		//sure, this'll probably work as intended
		this.drink = drink;
		this.salad = salad;
		this.sandwich = sandwich;
	}
	public String getName(){
		return(	this.drink.getName() +//\
				this.salad.getName() +//\
				this.sandwich.getName());
		/*keeping it all on one line
		 *maybe, slashes to concatenate
		 *lines might just be a C thing
		 *Revision:
		 *	After firing this through javac,
		 *	I can safely say that slashes for
		 *	line concatenation is just a C thing.
		 */
	}
	public double getPrice(){
		//i'm taking the easy way out here and
		//just using several if statements
		if(this.drink.getPrice() < this.salad.getPrice() && this.drink.getPrice() < this.sandwich.getPrice()){
			//if the drink costs the least
			return this.salad.getPrice() + this.sandwich.getPrice();
		}
		if(this.salad.getPrice() < this.drink.getPrice() && this.salad.getPrice() < this.sandwich.getPrice()){
			//if the salad costs the least
			return this.drink.getPrice() + this.sandwich.getPrice();
		}
		if(this.sandwich.getPrice() < this.drink.getPrice() && this.sandwich.getPrice() < this.salad.getPrice()){
			//if the sandwich costs the least
			return this.drink.getPrice() + this.salad.getPrice();
		}
		//if all else fails
		return Double.NaN;
	}
}

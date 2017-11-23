public class Sandwich implements MenuItem
{
   private String name;
   private double price;
   
   public Sandwich(String n, double p)
   {
      name = n;
      price = p;
   }
   
   public String getName()
   { return name;}
   
   public double getPrice()
   { return price;}
}
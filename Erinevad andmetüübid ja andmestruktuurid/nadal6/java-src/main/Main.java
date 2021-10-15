package main;

public class Main {

    public static void main(String[] args) {

        Dog germanShepherd = new Dog(48, 35, "German Shepherd");
        Dog greyHound = new Dog(72, 33, "Greyhound.");
        Human english = new Human(13, 80, "English", "English");

        greyHound.bark();
        germanShepherd.bark();
        english.talk();

        greyHound.whatAmI();
        english.whatAmI();
        germanShepherd.whatAmI();

    }
}

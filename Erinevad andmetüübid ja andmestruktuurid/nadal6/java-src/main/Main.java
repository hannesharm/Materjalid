package main;

public class Main {

    public static void main(String[] args) {

        Dog germanShepherd = new Dog(48, 35, "German Shepherd");
        Dog greyHound = new Dog(72, 33, "Greyhound");
        Human human = new Human(13, 80, "english");

        germanShepherd.bark();
        human.talk();

        greyHound.eat();
        human.eat();
    }
}

package main;

public class Human extends Animal {

    public Human(float maxRunningSpeed, float weight, String nationality) {
        super(2, maxRunningSpeed, weight, nationality);
    }

    public void talk() {
        System.out.printf("I am a %s!\n", breedName);
    }
}

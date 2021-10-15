package main;

public class Dog extends Animal {

    public Dog(float maxRunningSpeed, float weight, String breedName) {
        super(4, maxRunningSpeed, weight, breedName);
    }

    public void bark() {
        System.out.println("Bark!");
    }
}

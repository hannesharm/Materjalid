package main;

public abstract class Animal {
    public int numberOfLegs;
    public float maxRunningSpeed;
    public float weight;
    public boolean hasEaten;
    public String breedName;

    public Animal(int numberOfLegs, float maxRunningSpeed, float weight, String breedName) {
        this.numberOfLegs = numberOfLegs;
        this.maxRunningSpeed = maxRunningSpeed;
        this.weight = weight;
        this.hasEaten = false;
        this.breedName = breedName;
    }

    public void run() {
        System.out.printf("Running with speed of %f km/h\n", maxRunningSpeed);
    }

    public void eat() {
        System.out.println("Eating!");
        hasEaten = true;
    }
}

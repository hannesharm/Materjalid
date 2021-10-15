package main;

public class Human extends Animal {

    public String motherLanguage;

    public Human(float maxRunningSpeed, float weight, String motherLanguage, String nationality) {
        super(2, maxRunningSpeed, weight, nationality);
        this.motherLanguage = motherLanguage;
    }

    public void talk() {
        System.out.printf("Talking in %s!\n", motherLanguage);
    }
}

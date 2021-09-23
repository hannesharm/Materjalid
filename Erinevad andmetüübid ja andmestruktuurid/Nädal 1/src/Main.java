
public class Main {

    public static void main(String[] args) {

        char a = 'A';
        char b = a;

        System.out.println(a);
        System.out.println(b);

        Auto lahe = new Auto("Sinine", 1500);
        Auto kole = lahe;

        lahe.kaal = 2000;

        System.out.println(lahe);
        System.out.println(kole);
    }
}

class Auto {

    String varv;
    int kaal;

    public Auto(String varv, int kaal) {
        this.varv = varv;
        this.kaal = kaal;

    }
}



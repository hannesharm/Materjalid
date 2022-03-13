import java.time.LocalDate;
import java.util.Date;

public class Main {
    public static void main(String[] args) {
        LocalDate now = LocalDate.now();
        System.out.println(now.getYear());
        System.out.println(now.getDayOfMonth());

    }


    public class Car {
        LocalDate registration;
        Category category;
        Body bodyType;
        String color;
        EngineDisplacement displacement;
    }

    public enum Category {
        Bus,
        Car,
        Motorcycle,
        Truck
    }

    public enum Body {
        Hatchback,
        Sedan,
        SUV,
        Cabrio
    }

    public class EngineDisplacement {
        int size;
        String unit;
    }
}

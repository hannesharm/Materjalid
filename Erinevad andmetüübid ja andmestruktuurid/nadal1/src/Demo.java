import java.util.Collection;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Demo {


    public static void main(String[] args) {
        List<String> list1 = List.of("element1", "Element222222");
        List<String> list2 = List.of("element3", "Element4");
        List<String> list3 = List.of("element5", "Element6");


        var streamed = list1
                .stream()
                .map(String::length)
                .filter(e -> e > 10)
                .collect(Collectors.toList());

        System.out.println(streamed);

        var all = Stream.of(list1, list2, list3)
                .flatMap(Collection::stream)
                .collect(Collectors.toList());

        System.out.println(all);

    }
}

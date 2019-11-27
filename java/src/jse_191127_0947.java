import java.util.ArrayList;
import java.util.List;

/**
 * Java 8 Groussard: Les collections
 * Exercises with List type
 */
public class jse_191127_0947 {

    public static void main(String[] args) {
        Listing listing = new Listing();
        listing.deleteList();
    }
}

class Listing {

    private List<String> lst;

    Listing() {
        this.lst = new ArrayList<>();
    }

    public void deleteList() {
        lst.add("One");
        lst.add("Two");
        lst.add("Three");

        while (!lst.isEmpty()) {
            lst.remove(0);
        }
        System.out.println(lst.size());
    }
}

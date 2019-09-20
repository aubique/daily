import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;
import java.util.TreeMap;

public class jse_191119_1348 {

    public static void main(String[] args) {
//        showRemainder();
//        useList("tmp/test.dat");
        useDictionary("tmp/alice30.txt");
    }

    private static void showRemainder() {
        double firstValue = 20.00d;
        double secondValue = 80.00d;
        double total = ((firstValue + secondValue) * 100.00d);
        double remainder = total % 40.00d;
        boolean isNoRemainder = remainder == 0 ? true : false;
        System.out.println("Remainder doesn't exist: " + isNoRemainder);
        if (!isNoRemainder) {
            System.out.println("Got some remainder");
        }
    }

    private static void useList(String filename) {
        ArrayList<Integer> countList;
        Scanner data = null;
        int idx;

        try {
            data = new Scanner(new File(filename));
        } catch (FileNotFoundException e) {
            System.out.println("Not found");
            e.printStackTrace();
            System.exit(0);
        }

        countList = new ArrayList<Integer>(10);
        for (int i = 0; i < 10; i++) {
            countList.add(i, 0);
        }

        while (data.hasNextInt()) {
            idx = data.nextInt();
            countList.set(idx, countList.get(idx) + 1);
        }

        idx = 0;
        for (int i = 0; i < countList.size(); i++, idx++) {
            System.out.println(i + " occured " + countList.get(i) + " times.");
        }
    }

    private static void useDictionary(String filename) {
        Scanner data = null;
        TreeMap<String, Integer> count;
        String key, word;
        Integer value, wordCount;

        try {
            data = new Scanner(new File(filename));
        } catch (FileNotFoundException e) {
            System.out.println(filename + "is not found");
            e.printStackTrace();
            System.exit(0);
        }

        count = new TreeMap<String, Integer>();
        while (data.hasNext()) {
            word = data.next().toLowerCase();
            wordCount = count.get(word);
            if (wordCount == null) {
                wordCount = 0;
            }
            count.put(word, ++wordCount);
        }

        for (Iterator<String> iter = count.keySet().iterator(); iter.hasNext(); ) {
            key = iter.next();
            value = count.get(key);
            System.out.printf("%-20s occured %5d times%n", key, value);
        }
    }
}

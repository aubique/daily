import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class jse_191209_0714 {

    public static void main(String[] args) {
        System.out.println(SongDecoder("AWUBWUBABCWUB"));
        System.out.println(decodeSongByStream("AWUBWUBABCWUB"));
    }

    /**
     * CodeWars: Dubstep
     * https://www.codewars.com/kata/dubstep/java
     */
    public static String SongDecoder(String song) {
        List<String> initalText = new ArrayList<>();
        Arrays.asList(song.split("WUB"))
                .forEach(s -> {
                    if (!s.isEmpty()) initalText.add(s);
                });
        return String.join(" ", initalText);
    }
    public static String decodeSongByStream(String text) {
        return Arrays.stream(text.split(text)).
                filter(item -> !"".equals(item))
                .collect(Collectors.joining(" "));
    }
}

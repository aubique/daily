public class jse_191120_2230 {
// Codewars: count sheeps exercise

    public static void main(String[] args) {
        Boolean[] sheepArray = {true, true, true, false,
                true, true, true, true,
                true, false, true, false,
                true, false, false, true,
                true, true, true, true,
                false, null, true, true};
        System.out.println(countSheeps(sheepArray));
    }

    public static int countSheeps(Boolean[] arrayOfSheeps) {
        int numberOfShips = 0;
        for (int i = 0; i < arrayOfSheeps.length; i++) {
            if (arrayOfSheeps[i] != null && arrayOfSheeps[i]) {
                numberOfShips++;
            }
        }
        return numberOfShips;
    }
}

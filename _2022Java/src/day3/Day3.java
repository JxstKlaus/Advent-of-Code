package day3;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public class Day3 {
    public static void main(String[] args) throws Exception{
        BufferedReader bufferedReader = new BufferedReader(new FileReader("inputs\\day3_input.txt"));

        String testInput = """
                vJrwpWtwJgWrhcsFMMfFFhFp
                jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
                PmmdzqPrVvPwwTWBwg
                wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
                ttgJtRGJQctTZtZT
                CrZsJsPPZsGzwwsLwLmpwMDw""";

        String letters = "abcdefghijklmnopqrstuvwxyz";
        int lettersLength = letters.length();

        int priorities = 0;
        int commonBadgePriorities = 0;

        ArrayList<String> commonThree = new ArrayList<>();

        String line;
        while ((line = bufferedReader.readLine()) != null){
        //for(String line : testInput.split("\n")){
            int middle = line.length()/2;
            char[][] splitLine = {line.substring(0, middle).toCharArray(), line.substring(middle).toCharArray()};
            for (char char1 : splitLine[0]){
                boolean found = new String(splitLine[1]).indexOf(char1) != -1;

                if (found) {
                    if (Character.isLowerCase(char1)) priorities += letters.indexOf(char1) + 1;
                    else priorities += letters.indexOf(Character.toLowerCase(char1)) + 1 + lettersLength;
                    break;
                }
            }

            //part 2

            commonThree.add(line.strip());
            if (commonThree.size() == 3){
                for (char c : line.toCharArray()){
                    if ((commonThree.get(0).indexOf(c) != -1) && (commonThree.get(1).indexOf(c) != -1)){
                        if (Character.isLowerCase(c)) commonBadgePriorities += letters.indexOf(c) + 1;
                        else commonBadgePriorities += letters.indexOf(Character.toLowerCase(c)) + 1 + lettersLength;
                        commonThree = new ArrayList<>();
                        break;
                    }
                }
            }
        }
        System.out.println("Day 3 part 1 answer: " + priorities);
        System.out.println("Day 3 part 2 aswer: " + commonBadgePriorities);
    }
}

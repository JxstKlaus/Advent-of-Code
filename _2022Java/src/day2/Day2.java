package day2;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.HashMap;
import java.util.Map;

public class Day2 {
    final static int rock = 1;
    final static int paper = 2;
    final static int scissors = 3;

    final static int win = 6;
    final static int draw = 3;
    final static int loss = 0;

    public static void main(String[] args) throws Exception {
        Map<String,Integer> hands = new HashMap<>();

        hands.put("A",rock);
        hands.put("B",paper);
        hands.put("C",scissors);
        hands.put("X",rock);
        hands.put("Y",paper);
        hands.put("Z",scissors);

        String testData = """
                A Y
                B X
                C Z""";

        BufferedReader bufferedReader = new BufferedReader(new FileReader("inputs\\day2_input.txt"));

        String line;
        int score=0;
        int predictScore = 0;
        while ((line = bufferedReader.readLine()) != null){
            String[] match = line.trim().split(" ");

            if (    (hands.get(match[1]) == 1 && hands.get(match[0]) == 3) ||
                    (hands.get(match[1]) == 2 && hands.get(match[0]) == 1) ||
                    (hands.get(match[1]) == 3 && hands.get(match[0]) == 2)
            ) score += win;
            else if (hands.get(match[0]) == hands.get(match[1])) score += draw;

            score += hands.get(match[1]);

            //part 2 ------------------------------

            //X:loss, Y: draw, Z: win
            switch (match[1]){
                case "Z" -> predictScore += 6;
                case "Y" -> predictScore += 3;
            }
            if (match[1].equals("X")){
                switch (match[0]){
                    case "A" -> predictScore += scissors;
                    case "B" -> predictScore += rock;
                    case "C" -> predictScore += paper;
                }
            }
            else if (match[1].equals("Z")){
                switch (match[0]){
                    case "A" -> predictScore += paper;
                    case "B" -> predictScore += scissors;
                    case "C" -> predictScore += rock;
                }
            }
            else predictScore += hands.get(match[0]);

        }

        System.out.println("Day 2 part 1 answer: " + score);
        System.out.println("Day 2 part 2 answer: " + predictScore);

    }
}

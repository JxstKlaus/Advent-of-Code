package day1;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static void main(String[] args) {
        String filePath = "src\\inputs\\Day1_input.txt";

        ArrayList<Integer> caloriesTotal = new ArrayList<>();
        ArrayList<Integer> caloriesPerElf = new ArrayList<>();;
        int mostCaloriesCarried=0;

        try{
            FileReader fileReader = new FileReader(filePath);
            BufferedReader bufferedReader = new BufferedReader(fileReader);

            String line;
            while ((line = bufferedReader.readLine()) != null){
                if(line.trim().isEmpty()){
                    int sum = 0;
                    for (int n : caloriesPerElf) sum += n;
                    caloriesTotal.add(sum);
                    if (sum > mostCaloriesCarried) mostCaloriesCarried = sum;
                    caloriesPerElf = new ArrayList<>();
                }
                else caloriesPerElf.add(Integer.parseInt(line));
            }
        }
        catch (IOException e){
            e.printStackTrace();
        }

        System.out.println("Day 1 part 1 answer: "+mostCaloriesCarried);

        //sorting the list
        Collections.sort(caloriesTotal, Collections.reverseOrder());

        int topThree = 0;
        for (int i = 0; i<3; i++) topThree += caloriesTotal.get(i);

        System.out.println("Day 1 part 2 answer: "+topThree);

    }
}

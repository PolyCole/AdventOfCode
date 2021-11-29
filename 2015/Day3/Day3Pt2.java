package aoc;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

/*
 * Author: Cole Polyak
 * 26 February 2018
 * Advent of Code 2015 Day 3 Pt 2
 * 
 */

// TODO Determine more elegant solution to array of houses creation.
// TODO Implement safe file initialization
// TODO Look into more elegant solution for part 2.


public class Day3Pt2 {

	public static void main(String[] args) {
		
		// File initialization.
		Scanner file = null;
		
		try
		{
			file = new Scanner(new FileInputStream("Day3Input.txt"));
		}
		catch(FileNotFoundException e)
		{
			e.printStackTrace();
			System.exit(1);
		}
		
		// Kinda clumsy array creation...
		int[][] arr = new int[5000][5000];
		
		// Santa's initial position.
		int santaX = 2499;
		int santaY = 2499;
		
		// Robo-Santa's initial position.
		int roboSantaX = 2499;
		int roboSantaY = 2499;
		
		// If determiningBoolean is true - instruction is for Santa. Else, robo.
		boolean determiningBoolean = true;
		
		String input = file.next();

		int currentIndex = 0;
		
		// Loops over input to determine command.
		for(int i = 0; i < input.length(); ++i)
		{
			String cur = input.substring(currentIndex, currentIndex+1);
			
			// Move left
			if("<".equals(cur))
			{
				if(determiningBoolean)
				{
					System.out.println("Santa: <");
					++arr[santaX][santaY];
					++arr[santaX-1][santaY];
					--santaX;
				}
				else
				{
					System.out.println("Robo-Santa: <");
					++arr[roboSantaX][roboSantaY];
					++arr[roboSantaX-1][roboSantaY];
					--roboSantaX;
				}
			}
			
			// Move right
			else if(">".equals(cur))
			{
				if(determiningBoolean)
				{
					System.out.println("Santa: >");
					++arr[santaX][santaY];
					++arr[santaX+1][santaY];
					++santaX;
				}
				else
				{
					System.out.println("Robo-Santa: >");
					++arr[roboSantaX][roboSantaY];
					++arr[roboSantaX+1][roboSantaY];
					++roboSantaX;
				}
			}
			
			// Move down
			else if("v".equals(cur))
			{
				if(determiningBoolean)
				{
					System.out.println("Santa: v");
					++arr[santaX][santaY];
					++arr[santaX][santaY-1];
					--santaY;
				}
				else
				{
					System.out.println("Robo-Santa: v");
					++arr[roboSantaX][roboSantaY];
					++arr[roboSantaX][roboSantaY-1];
					--roboSantaY;
				}
			}
			
			// Move up
			else if("^".equals(cur))
			{
				if(determiningBoolean)
				{
					System.out.println("Santa: ^");
					++arr[santaX][santaY];
					++arr[santaX][santaY+1];
					++santaY;
				}
				else
				{
					System.out.println("Robo-Santa: ^");
					++arr[roboSantaX][roboSantaY];
					++arr[roboSantaX][roboSantaY+1];
					++roboSantaY;
				}
			}
			++currentIndex;
			
			// Toggles which santa the input is going to.
			determiningBoolean = !(determiningBoolean);
		}
		
		// Loop to sum houses receiving atleast one gift.
		int housesReceivingAtLeastOne = 0;
		
		for(int i = 0; i < arr.length; ++i)
		{
			for(int j = 0; j < arr[i].length; ++j)
			{
				if(arr[i][j] >= 1)
				{
					++housesReceivingAtLeastOne; 
				}
			}
		}
		
		// And output.
		System.out.println("Houses receiving atleast one gift: " + housesReceivingAtLeastOne);
		
		

	}

}

package aoc;

//Import block
import java.io.FileNotFoundException;
import java.io.FileInputStream;
import java.util.Scanner;

public class Day1 {

	/*
	 * Author: Cole Polyak
	 * Advent of Code 2017 Day 1
	 * 01 December 2017
	 * 
	 */
	
	public static void main(String[] args) {
		
		Scanner keyboard = null;
		
		//Try catch block to set up Scanner
		try
		{
			keyboard = new Scanner(new FileInputStream("inputDay1.txt"));
		}
		catch(FileNotFoundException e)
		{
			System.out.println("File not found.");
			System.exit(0);
		}
		
		//Defining number array. File format has total number of ints as first line in the file.
		int[] nums = new int[keyboard.nextInt()];
		
		//Initializing our array.
		int index = 0;
		while(keyboard.hasNextInt())
		{
			nums[index] = keyboard.nextInt();
			++index;
		}
		
		
		int sum = 0;
		
		// Looping over array.
		for(int i = 0; i < nums.length; ++i)
		{
			int current; int current2;
			
			//If else statement assigns our current scoped numbers. If the last number in the sequence 
			// is being looked at, the last number and first number are paired.
			if(i == nums.length-1)
			{
				current = nums[i];
				current2 = nums[0];
			}
			else
			{
				current = nums[i];
				current2 = nums[i+1];
			}
			
			//Checks if the numbers are identical and sums if they are.
			if(current == current2)
			{
				sum += current;
			}
			
		}
		
		
		int secondSum = 0;

		// Defines the index exactly half the array away from the beginning.
		int currentSecondIndex = (nums.length / 2)-1;
		
		// Checks if the current number equals the number half the array away.
		for(int i = 0; i < nums.length; ++i)
		{
			int cur = nums[i];
			
			// Loops halfway position to avoid ArrayOutOfBoundsException
			if(cur == nums[(++currentSecondIndex + 2042) % 2042])
			{
				sum += cur;
			}
		}
		
		//And output.
		System.out.println("Part 1 --The sum of the consecutive numbers are " + sum);
		
		//And output.
		System.out.println("Part 2 --The sum of numbers halfway away from each other is: " + secondSum);
		
		keyboard.close();
	}

}

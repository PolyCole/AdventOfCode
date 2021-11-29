package aoc;

import java.util.Scanner;
import java.io.FileInputStream;
import java.io.FileNotFoundException;

/*
 * Author: Cole Polyak
 * 23 February 2018
 * Advent Of Code 2017 Day 2
 */

// TODO Figure out a way to determine needed array size. ArrayLists?
// TODO Implement safe file input.

public class Day2 {

	public static void main(String[] args) {
		
		// FileInputStream setup.
		Scanner file = null;
		
		try
		{
			file = new Scanner(new FileInputStream("Day2Input.txt"));
		}
		catch(FileNotFoundException e)
		{
			System.out.println("File not found...");
			System.exit(0);
		}
		
		// Creating spreadsheet array
		int[][] spreadsheet = new int[16][16];
		
		// Initializes array.
		for(int i = 0; i < spreadsheet.length; ++i)
		{
			for(int j = 0; j < spreadsheet[i].length; ++j)
			{
				spreadsheet[i][j] = file.nextInt();
			}
		}
		
		// Part 1
		int sum = 0;
		
		// Adds the difference between the max and min of each line.
		for(int i = 0; i < spreadsheet.length; ++i)
		{
			int max = 0;
			int min = spreadsheet[0][0];
			
			for(int j = 0; j < spreadsheet[i].length; ++j)
			{
				int cur = spreadsheet[i][j];
				
				if(cur > max) { max = cur; }
				if(cur < min) { min = cur; }
			}
			
			int diff = max - min;
			sum += diff;
		}

		// Part 2
		int secondSum = 0;

		// Adds the result of the two evenly divisible numbers in each row.
		for(int i = 0; i < spreadsheet.length; ++i)
		{
			int toBeAdded = 0;

			for(int j = 0; j < spreadsheet[i].length; ++j)
			{
				int cur = spreadsheet[i][j];
				for(int k = 0; k < spreadsheet[i].length; ++k)
				{
					if(spreadsheet[i][k] == cur)
					{
						continue;
					}
					if(cur % spreadsheet[i][k] == 0)
					{
						toBeAdded += cur / spreadsheet[i][k];
					}
				}

			}
			secondSum += toBeAdded;
		}
		
		// And output.
		System.out.println("The checksum for this sheet is: " + sum);
		
		System.out.println("The sum of evenly disible numbers is: " + secondSum);
		
		file.close();
	}

}

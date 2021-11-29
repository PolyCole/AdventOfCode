package aoc;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

/*
 * Author: Cole Polyak
 * 25 February 2018
 * Advent of Code 2015 Day 3 Pt. 1
 * 
 */

// TODO Determine more elegant solution to array of houses creation.
// TODO Implement safe file initialization

public class Day3Pt1 {

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
		int x = 2499;
		int y = 2499;
		
		// File is one line, so it can be read in all at once.
		String input = file.next();
		int currentIndex = 0;
		
		// Iterates over file.
		for(int i = 0; i < input.length(); ++i)
		{
			String cur = input.substring(currentIndex, currentIndex+1);
			
			// Move left
			if("<".equals(cur))
			{
				System.out.println("<");
				++arr[x][y];
				++arr[x-1][y];
				--x;
			}
			
			// Move right
			else if(">".equals(cur))
			{
				System.out.println(">");
				++arr[x][y];
				++arr[x+1][y];
				++x;
			}
			
			// Move down
			else if("v".equals(cur))
			{
				System.out.println("V");
				++arr[x][y];
				++arr[x][y-1];
				--y;
			}
			
			// Move up
			else if("^".equals(cur))
			{
				System.out.println("^");
				++arr[x][y];
				++arr[x][y+1];
				++y;
			}
			++currentIndex;
		}
		
		// Loop to determine how many houses got atleast one gift.
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

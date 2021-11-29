package aoc;

// Import block
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;


/*
 * Author: Cole Polyak
 * Advent of Code 2015 Day 1
 * 25 February 2018
 *
 */

public class Day1 {

	public static Scanner file = null;

	public static void main(String[] args) {

		// Safe file input stream initialization.
		Scanner keyboard = new Scanner(System.in);
		System.out.println("Please input file name: ");
		
		initFile(keyboard.next());
		
		// The entire file can be read into one string since the file is one line.
		System.out.println("File success. Reading file...");
		String input = file.next();
		
		// Closing our scanners.
		keyboard.close();
		file.close();
	
		
		int currentFloor = 0;
		int curIndex = 0;
		
		// Loops infinitely.
		while(true)
		{
			// Tries to read in next character.
			try
			{
				// Up a floor
				if("(".equals(input.substring(curIndex, curIndex+1)))
				{
					System.out.println("Plus 1");
					++currentFloor;
				}
				
				// Down a floor
				else if(")".equals(input.substring(curIndex, curIndex+1)))
				{
					System.out.println("Minus 1");
					--currentFloor;
				}
				
				++curIndex;
						
			}
			// When the file runs out of characters, an error will be thrown. Breaks loop.
			catch(StringIndexOutOfBoundsException e)
			{
				break;
			}
		}
		
		int currentFloorTwo = 0;
		int curIndexTwo = 0;
		
		
		// Loops until the current floor is negative.
		while(currentFloor != -1)
		{
			try
			{
				// Up a floor.
				if("(".equals(input.substring(curIndex, curIndex+1)))
				{
					System.out.println("Plus 1");
					++currentFloor;
				}
				
				// Down a floor.
				else if(")".equals(input.substring(curIndex, curIndex+1)))
				{
					System.out.println("Minus 1");
					--currentFloor;
				}
				
				++curIndex;
						
			}
			// Catches the end of the file and breaks the infinite loop.
			catch(StringIndexOutOfBoundsException e)
			{
				break;
			}
		}
		
		
		// Part 1 output.
		System.out.println("--------------------------");
		System.out.println("The final floor is: " + currentFloor + ".");
		System.out.println("--------------------------");
		
		
		// Part 2 output.
		System.out.println("--------------------------");
		System.out.println("The index that causes a negative floor is: " + curIndexTwo );
		System.out.println("Current Floor: " + currentFloorTwo);
		System.out.println("--------------------------");
		
		

	}

	// Safe fileinputstream creation.
	public static String initFile(String fileName)
	{
		Scanner keyboard = new Scanner(System.in);

		// Quits to prevent infinite loop.
		if("".equals(fileName))
		{
			System.out.println("Exiting...");
			System.exit(0);
		}
		
		// Tries to create input stream.
		try
		{
			file = new Scanner(new FileInputStream(fileName));
		}
		catch(FileNotFoundException e)
		{
			// Infinite until valid file is inputted.
			System.out.println("File not found. Please double check filename and try again. Hit ENTER to quit.");
			initFile(keyboard.next());
		}

		keyboard.close();
		return fileName;
	}
}

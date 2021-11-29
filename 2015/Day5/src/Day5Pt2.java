package aoc;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

/*
*
* Author: Cole Polyak
* 13 May 2018
* Advent of Code 2015 Day 5 Part 2
* 
*/

public class Day5Pt2 
{
	public static void main(String[] args)
	{
		
		Scanner file = null;

		// Reading in file.
		try
		{
			file = new Scanner(new FileInputStream("Day5InputTest.txt"));
		}
		catch(FileNotFoundException e)
		{
			e.printStackTrace();
		}

		int niceCount = 0;
		
		while(file.hasNext())
		{
			String cur = file.next();

			// Checks if both conditions are met.
			if(sandwhich(cur) && doublePair(cur))
			{
				niceCount++;
			}
		}

		System.out.println("Nice count: " + niceCount);
	}

	// Checks for the "sandwhich" patter of two identical characters sandwhiching another character.
	public static boolean sandwhich(String cur)
	{
		for(int i = 0; i < cur.length(); ++i)
		{
			try
			{
				if(cur.substring(i, i+1).equals(cur.substring(i+2,i+3))) {return true;}
			}
			catch(StringIndexOutOfBoundsException e) { break;}
		}

		return false;
	}
	
	// Checks for two pairs of double letters.
	public static boolean doublePair(String cur)
	{
		String target = null;
		
		for(int i = 0; i < cur.length(); ++i)
		{
			try
			{
				// What we're looking for.
				target = cur.substring(i, i+2);
				
				// Everything else.
				String leftover = cur.subSequence(0, i) + cur.substring(i+2);
				
				if(leftover.contains(target)) { System.out.println(target); return true;}
				
			} catch(StringIndexOutOfBoundsException e) { continue;}
		}
		
		return false;
	}
}

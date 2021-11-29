package aoc;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

/*
*
* Author: Cole Polyak
* 13 May 2018
* Advent of Code 2015 Day 5 Part 1
* 
*/

public class Day5Pt1 
{
	public static void main(String[] args)
	{
		Scanner file = null;
		
		// Reading in file.
		try
		{
			file = new Scanner(new FileInputStream("Day5Input.txt"));
		}
		catch(FileNotFoundException e)
		{
			e.printStackTrace();
		}
		
		int niceCount = 0;
		
		while(file.hasNext())
		{
			String cur = file.next();
			
			// First checks if the phrase contains an immediate naughty phrase.
			if(!(containsPhrases(cur)))
			{
				// If it doesn't and it contains both other conditions, we're good.
				if(vowelCount(cur) && doubleLetters(cur))
				{
					niceCount++;
				}
			}
		}
		System.out.println("Nice count: " + niceCount);
	}
	
	// Checks for a pair of double letters.
	public static boolean doubleLetters(String cur)
	{
		for(int i = 0; i < cur.length(); ++i)
		{
			try
			{
				String curSub = cur.substring(i, i+1);
				if(curSub.equals(cur.substring(i+1,i+2))) { return true;}
			}
			catch(Exception e) { break;}
		}
		return false;
	}
	
	// Counts number of vowels.
	public static boolean vowelCount(String cur)
	{
		String vowels = "aeiou";
		int numVowels = 0;
		
		for(int i = 0; i < cur.length(); ++i)
		{
			String curSub = cur.substring(i, i+1);
			if(vowels.indexOf(curSub) != -1) { numVowels++;}
		}
		
		return numVowels >= 3;
		
	}
	
	// Checks if the string contains any of the naughty phrases.
	public static boolean containsPhrases(String cur)
	{
		String[] arr = {"ab","cd","pq","xy"};
		boolean discovered = false;
		
		for(int i = 0; i < cur.length(); ++i)
		{
			try
			{
				String curSub = cur.substring(i, i+2);
				for(int j = 0; j < arr.length; ++j)
				{
					if(curSub.equals(arr[j])) { discovered = true;}
				}
			}
			catch(Exception e) { break;}
			
		}
		return discovered;
	}
}

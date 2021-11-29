package aoc;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

/*
 * Author: Cole Polyak
 * 21 February 2018
 * Advent of Code 2015 Day 2
 * 
 */

// TODO Implement safe file initialization. 
// TODO FindMax and FindExtra feel clunky.

public class Day2 {

	public static void main(String[] args) {
		
		// FileInputStream initialization.
		Scanner file = null;
		
		try
		{
			file  = new Scanner(new FileInputStream("Day2Input.txt"));
		}
		catch(FileNotFoundException e)
		{
			e.printStackTrace();
			System.exit(0);
		}
			
		// Macro sum variables.
		int wrappingPaperAreaSum = 0;
		int ribbonLengthSum = 0;
		
		
		while(file.hasNextLine()) 
		{
			// Reads in line
			String testing =file.nextLine();
			
			// Splits on x.
			String[] stringArray = testing.split("x");
			
			int l = Integer.parseInt(stringArray[0]);
			int w = Integer.parseInt(stringArray[1]);
			int h = Integer.parseInt(stringArray[2]);
		
			int max = findMax(l,w,h);
			int ribbonLength = 0;
			
			// Determining ribbon length integers.
			if(max == l)
			{
				ribbonLength += (2*w) + (2*h);
			}
			else if(max == w)
			{
				ribbonLength += (2*l) + (2*h);
			}
			else
			{
				ribbonLength += (2*l) + (2*w);
			}
			
			// Wrapping Paper Area calculations
			int wrappingPaperArea = (2 * ((l * w) + (w * h) + (h * l))) 
									+ findExtra(l,w,h);
			
			// Adding the bow.
			ribbonLength += (l*w*h);
			
			ribbonLengthSum += ribbonLength;
			wrappingPaperAreaSum += wrappingPaperArea;
		}

		// And output.
		System.out.println("Total area of wrapping paper needed: " + wrappingPaperAreaSum);
		System.out.println("Total length of ribbon needed: " + ribbonLengthSum);
		
	}
	
	// Method excepts three integers and returns the largest of them.
	public static int findMax(int l, int w, int h)
	{
		if((l >= w) && (l >= h))
		{
			return l;
		}
		else if((w >= l) && (w >= h))
		{
			return w;
		}
		else
		{
			return h;
		}
	}

	// Method returns the minimum extra area needed.
	public static int findExtra(int l, int w, int h)
	{
		int a = l*w;
		int b = w*h;
		int c = l*h;
		
		if((a <= b) && (a <= c))
		{
			return a;
		}
		else if((b <= a) && (b <= c))
		{
			return b;
		}
		else
		{
			return c;
		}
	}

}

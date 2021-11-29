package aoc;

import javax.xml.bind.DatatypeConverter;
import java.security.MessageDigest;
import java.util.Scanner;

/*
*
* Author: Cole Polyak
* 05 March 2018
* Advent of Code 2015 Day 4
* 
*/

public class Day4 {

	public static void main(String[] args)
	{
		Scanner keyboard = new Scanner(System.in);
		
		System.out.println("Please input given string");
		String input = keyboard.next();
		keyboard.close();
		
		System.out.println("The final MD5 hash with 5 zeroes is: " + Day4.get5Zero(input));
		System.out.println("The final MD5 hash with 6 zeroes is: " + Day4.get6Zero(input));
		
		
	}
	
	// Returns the smallest non-negative number needed make the first five digits 0.
	public static String get5Zero(String input)
	{
		int digit = 0;
		loop:
			while(true)
			{
				String output = Day4.getMD5(input + digit);
				if("00000".equals(output.substring(0, 5)))
				{
					break loop;
				}
				
				++digit;
			}
		return (input + digit);
		
	}
	
	// Returns the smallest non-negative number needed make the first six digits 0.
	public static String get6Zero(String input)
	{
		int digit = 0;
		loop:
			while(true)
			{
				String output = Day4.getMD5(input + digit);
				if("000000".equals(output.substring(0, 6)))
				{
					break loop;
				}
				
				++digit;
			}
		return (input + digit);
		
	}
	
	// Gets the MD5 hash for the inputted string.
	public static String getMD5(String str)
	{
			MessageDigest md;
			try 
			{
				// Declaring algorithm
				md = MessageDigest.getInstance("MD5");
				
				// Declaring format
				byte[] hash = md.digest(str.getBytes("UTF-8"));
				return bytesToHex(hash);
			} 
			catch(Exception e)
			{
				System.out.println("Exception caught...");
				e.printStackTrace();
			}
			
			return null;
			
	}
	
	// Making the hash readable.
	public static String bytesToHex(byte[] hash)
	{
		return DatatypeConverter.printHexBinary(hash);
	}

}

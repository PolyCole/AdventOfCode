import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Day1Pt2 {

	public static void main(String[] args) {
		
		Scanner file = null;
		
		try
		{
			file = new Scanner(new FileInputStream("Day1Input.txt"));
		}
		catch(FileNotFoundException e)
		{
			e.printStackTrace();
			System.exit(0);
		}

		file.useDelimiter(",");
		
		int directionFacing = 3;
		int x = 0;
		int y = 0;
		
		int duplicateX = 0, duplicateY = 0;
		
		
		ArrayList<Integer>xPositions = new ArrayList<Integer>();
		ArrayList<Integer>yPositions = new ArrayList<Integer>();
		
		int blocksAway = 0;
		
		outer:
		while(file.hasNext())
		{
			String cur = file.next().trim();
			System.out.println("Current instruction: " + cur);
			String direction = cur.substring(0, 1);
			int number = Integer.parseInt(cur.substring(1));
			
			
			if("R".equals(direction))
			{
				++directionFacing;
				directionFacing = (directionFacing +  4) % 4;
			}
			else
			{
				--directionFacing;
				directionFacing = (directionFacing + 4) % 4;
			}
			
			for(int i = 0; i < number; ++i)
			{
				switch(directionFacing)
				{
					// East
					case 0:
						System.out.println("FACING EAST");
						System.out.println("CHANGING X");
						++x;
						//blocksAway += number;
						break;
					// South
					case 1:
						System.out.println("FACING SOUTH");
						System.out.println("CHANGING Y");
						--y;
						//blocksAway -= number;
						break;
					// West
					case 2:
						System.out.println("FACING WEST");
						System.out.println("CHANGING X");
						--x;
						//blocksAway -= number;
						break;
						
					// North
					case 3:
						System.out.println("FACING NORTH");
						System.out.println("CHANGING Y");
						++y;
						//blocksAway += number;
						break;
					default:
						System.out.println("DEFAULT CASE... NOT GOOD.");
						break;
				}
				
				xPositions.add(x);
				yPositions.add(y);
			}
			
			System.out.println("X: " + x);
			System.out.println("Y: " + y + "\n\n");
			
			for(int i = 0; i < xPositions.size(); ++i) 
			{
				System.out.println("xPositions(" + i + ") = " + xPositions.get(i));
				System.out.println("yPositions(" + i + ") = " + yPositions.get(i));
				System.out.println("\n");
			}
			
			System.out.println("\n\n");
			
			for(int i = 0; i < xPositions.size(); ++i)
			{
				int curX = xPositions.get(i);				
				int curY = yPositions.get(i);
				
				System.out.println("CURx: " + curX);
				System.out.println("CURy: " + curY + "\n");
				
				if((x == curX && y == curY) && (x != (xPositions.size()) && y != (yPositions.size())))
				{
					duplicateX = curX;
					duplicateY = curY;
				}
			}
			
			
			System.out.println("DUPLICATE COORDS: " + duplicateX + " and " + duplicateY);
			blocksAway += (Math.abs(x-duplicateX) + Math.abs(y-duplicateY));
			
			
		}
		
		System.out.println("The first location you visit twice is " + (blocksAway/2) + " blocks away");
		
		

	}

}

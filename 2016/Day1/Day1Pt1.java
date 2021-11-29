import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Day1Pt1 {

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
		
		int blocksAway = 0;
		
		
		while(file.hasNext())
		{
			String cur = file.next().trim();
			
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
			
			switch(directionFacing)
			{
				// East
				case 0:
					x += number;
					blocksAway += number;
					break;
				// South
				case 1:
					y -= number;
					blocksAway -= number;
					break;
				// West
				case 2:
					x -= number;
					blocksAway -= number;
					break;
				// North
				case 3:
					y += number;
					blocksAway += number;
					break;
				default:
					System.out.println("DEFAULT CASE... NOT GOOD.");
					break;
			}
		}
		
		System.out.println("You end up " + blocksAway + " blocks away from Easter Bunny HQ");
		
		

	}

}

package final_project;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class nearestNeighborDriver {

	public static void main(String[] args) throws FileNotFoundException {

		diagram();
		
		try {
			File file = new File("data.txt");
			FileWriter fw = new FileWriter("data.txt");
			
			//writes to the file. creating our data.
			fw.write("Building 1, Building 2, Building 3, Building 4, Building 5, Building 6, Building 7"
					+"\n12, 12, 10, 9, 8, 12, 11, 3, 7, 9, 6, 11, 10");
			fw.close();
			
			Scanner scan = new Scanner(file);
			while(scan.hasNextLine()) {
				nearestNeighborApp data = new nearestNeighborApp();
				//reads the first line of information in the file.
				String buildings = scan.nextLine();
				data.locations(buildings);
				//reads the next line of information in the file.
				String roads = scan.nextLine();
				data.paths(roads);
			}
			scan.close();
		}
		catch(IOException e){
			System.out.println("An error occurred:");
			e.printStackTrace();
		}
		
		
		
	}

	public static void diagram() {
		System.out.println("			(2)-----------------(4)"
				+"\n 			-  -		   - - -"
				+"\n 		       -    -		  -  -  -"
				+"\n		      -      - 		-    -    -"
				+"\n 		     -        -	      -      -      -"
				+"\n 		    -          -    -        -        -"
				+"\n 		  (1)-----------(3)--        -          -"
				+"\n 		    -           -     --     -            -"
				+"\n 		     -          -         --(5)             -"
				+"\n 		      -         -          -    -             -"
				+"\n 		       -        -         -        -            -"
				+"\n 		        -       -        -            -          -"
				+"\n 		         -      -       -                -         -"
				+"\n 		          -     -      -                    -       -"
				+"\n 		           -    -     -                        -     -"
				+"\n 		            -   -    -                            -   -"
				+"\n 		             -  -   -                               - -"
				+"\n 		              ( 7 )----------------------------------(6)");
	}
}

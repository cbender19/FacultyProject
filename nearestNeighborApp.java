package final_project;

//import java.util.Arrays;

public class nearestNeighborApp {
	
	String[] list;
	String[] list2;
	int[] length = new int[7];
	
	public void locations(String lines) {
		this.list = lines.split(", ");
		//System.out.println(Arrays.toString(this.list));
	}
	
	public void paths(String lines) {
		this.list2 = lines.split(", ");
		//System.out.println(Arrays.toString(this.list2));
		
		shortestPath();
		shortestPath2();
		shortestPath3();
		shortestPath4();
		shortestPath5();
		shortestPath6();
		shortestPath7();
		
		lengthTraveled();
	}
	
	public void shortestPath() {
		if(Integer.parseInt(list2[0]) < Integer.parseInt(list2[1]) && Integer.parseInt(list2[0]) < Integer.parseInt(list2[2])) {
			System.out.println("False");
		}
		else if(Integer.parseInt(list2[1]) < Integer.parseInt(list2[0]) && Integer.parseInt(list2[1]) < Integer.parseInt(list2[2])){
			System.out.println("False");
		}
		else if(Integer.parseInt(list2[2]) < Integer.parseInt(list2[0]) && Integer.parseInt(list2[2]) < Integer.parseInt(list2[1])) {
			visited("Building 3");
			this.length[0] = 10;
		}
		else {
			System.out.println("False"); 
		}
	}
	
	public void shortestPath2() {
		if(Integer.parseInt(list2[3]) < Integer.parseInt(list2[4]) && Integer.parseInt(list2[3]) < Integer.parseInt(list2[6]) && Integer.parseInt(list2[3]) < Integer.parseInt(list2[7])) {
			System.out.println("False");
		}
		else if(Integer.parseInt(list2[4]) < Integer.parseInt(list2[3]) && Integer.parseInt(list2[4]) < Integer.parseInt(list2[6]) && Integer.parseInt(list2[4]) < Integer.parseInt(list2[7])){
			System.out.println("False");
		}
		else if(Integer.parseInt(list2[6]) < Integer.parseInt(list2[3]) && Integer.parseInt(list2[6]) < Integer.parseInt(list2[4]) && Integer.parseInt(list2[6]) < Integer.parseInt(list2[7])) {
			System.out.println("False");
		}
		else if(Integer.parseInt(list2[7]) < Integer.parseInt(list2[3]) && Integer.parseInt(list2[7]) < Integer.parseInt(list2[6]) && Integer.parseInt(list2[7]) < Integer.parseInt(list2[4])) {
			visited("Building 5");
			this.length[1] = 3;
		}
		else {
			System.out.println("False"); 
		}
	}
	
	public void shortestPath3() {
		if(Integer.parseInt(list2[8]) > Integer.parseInt(list2[10]) && Integer.parseInt(list2[8]) < Integer.parseInt(list2[11])) {
			visited("Building 7");
			this.length[2] = 7;
		}
		else if(Integer.parseInt(list2[10]) > Integer.parseInt(list2[8]) && Integer.parseInt(list2[10]) < Integer.parseInt(list2[11])) {
			System.out.println("False");
		}
		else if(Integer.parseInt(list2[11]) < Integer.parseInt(list2[8]) && Integer.parseInt(list2[11]) < Integer.parseInt(list2[10])) {
			System.out.println("False");
		}
		else {
			System.out.println("False");
		}
	}
	
	public void shortestPath4() {
		if(Integer.parseInt(list2[9]) < Integer.parseInt(list2[1]) && Integer.parseInt(list2[9]) < Integer.parseInt(list2[3])) {
			System.out.println("False");
		}
		else if(Integer.parseInt(list2[1]) < Integer.parseInt(list2[9]) && Integer.parseInt(list2[1]) < Integer.parseInt(list2[3])) {
			System.out.println("False");
		}
		else if(Integer.parseInt(list2[3]) < Integer.parseInt(list2[9]) && Integer.parseInt(list2[3]) < Integer.parseInt(list2[1])) {
			System.out.println("False");
		}
		else {
			visited("Building 6");
			this.length[3] = 9;
		}
	}
	
	public void shortestPath5() {
		if(Integer.parseInt(list2[12]) > Integer.parseInt(list2[10])) {
			visited("Building 4");
			this.length[4] = 10;
		}
		else if(Integer.parseInt(list2[10]) > Integer.parseInt(list2[12])) {
			System.out.println("False");
		}
		else {
			System.out.println("False");
		}
	}
	
	public void shortestPath6() {
		if(Integer.parseInt(list2[5]) > Integer.parseInt(list2[6]) && Integer.parseInt(list2[5]) > Integer.parseInt(list2[11])) {
			visited("Building 2");
			this.length[5] = 12;
		}
		else if(Integer.parseInt(list2[6]) > Integer.parseInt(list2[5]) && Integer.parseInt(list2[6]) < Integer.parseInt(list2[11])) {
			System.out.println("False");
		}
		else if(Integer.parseInt(list2[11]) > Integer.parseInt(list2[5]) && Integer.parseInt(list2[11]) < Integer.parseInt(list2[6])) {
			System.out.println("False");
		}
		else {
			System.out.println("False");
		}
	}
	
	public void shortestPath7() {
		if(Integer.parseInt(list2[0]) > Integer.parseInt(list2[4])) {
			visited("Building 1");
			this.length[6] = 12;
		}
		else if(Integer.parseInt(list2[4]) > Integer.parseInt(list2[0])) {
			System.out.println("False");
		}
		else {
			System.out.println("False");
		}
	}
	
	public void visited(String location) {
		if(location.equals("Building 3")) {
			System.out.println("\nStarting Location: \n" +list[0]);
			System.out.println(list[2]);
		}
		if(location.equals("Building 5")) {
			System.out.println(list[4]);
		}
		if(location.equals("Building 7")) {
			System.out.println(list[6]);
		}
		if(location.equals("Building 6")) {
			System.out.println(list[5]);
		}
		if(location.equals("Building 4")) {
			System.out.println(list[3]);
		}
		if(location.equals("Building 2")) {
			System.out.println(list[1]);
		}
		if(location.equals("Building 1")) {
			System.out.println(list[0] +"\nBack at Starting Location.");
		}
	}
	
	public void lengthTraveled() {
		int total = 0;
		total = length[0] + length[1] + length[2] + length[3] +length[4] + length[5] + length[6];
		System.out.println("\nTotal Distance Traveled: \n" +total +" miles");
	}
}

/*
 * File name: NetflixApp.java
 *
 * Programmer: Connor Bender
 * cjbende
 *
 * Date Dec 4, 2019
 *
 * Class: IT 168
 * Lecture Section: 10
 * Lecture Instructor: Allan Abotteen
 * Lab Section: 12
 * Lab Instructor: Dr. Abotteen
 */
package edu.ilstu;

import java.util.Scanner;

/**
 * <insert class description here>
 *
 * @author Connor Bender
 *
 */
public class NetflixApp
{

	/**
	 * @param args
	 */
	public static void main(String[] args)
	{
		Scanner scan = new Scanner(System.in);
		
		NetflixHandler movie = new NetflixHandler();
		
		menu();
		System.out.print("Please make your choice: ");
		int choice = scan.nextInt();
		
		while(choice >= 1 && choice <= 5 || choice != 1 && choice != 2 && choice != 3 && choice != 4 && choice != 5) {
				if(choice == 1) {
					movie.read();
					System.out.println("");
					menu();
				}
				else if(choice == 2) {
					movie.searchTitle();
					System.out.println("");
					menu();
				}
				else if(choice == 3) {
					movie.searchYear();
					System.out.println("");
					menu();
				}
				else if(choice == 4) {
					movie.makeRecommendations();
					System.out.println("");
					menu();
				}
				else if(choice == 5) {
					System.out.println("Thank you for using the database. Please come back next time.");
					System.exit(choice);
				}
				else if(choice != 1 && choice != 2 && choice != 3 && choice != 4 && choice != 5) {
					System.out.print("Please provide a valid input: ");
					choice = scan.nextInt();
				}
			}	
		scan.close();
	}
	
	private static void menu() {
		System.out.println("\t\t\t\tWelcome to the Netflix Database");
		System.out.println("\t\t\t   ==========================================");
		System.out.println("\t\t\t       1. Browse all movies.");
		System.out.println("\t\t\t       2. Search a based on title.");
		System.out.println("\t\t\t       3. Search a based on year.");
		System.out.println("\t\t\t       4. Top movies recommendation.");
		System.out.println("\t\t\t       5. Exit.");
		System.out.println("\t\t\t   ==========================================");
	}

}

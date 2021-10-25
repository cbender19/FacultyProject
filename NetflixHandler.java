/*
 * File name: NetflixHandler.java
 *
 * Programmer: Connor Bender
 * cjbende
 *
 * Date Dec 4, 2019
 *
 * Class: IT 168
 * Lecture Section: 10
 * Lecture Instructor: Dr. Abotteen
 * Lab Section: 12
 * Lab Instructor: Allan Buckley
 */

package edu.ilstu;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

/**
 * <insert class description here>
 *
 * @author Connor Bender
 *
 */
public class NetflixHandler
{
	Scanner input = new Scanner(System.in);
	
	private int actualSize;
	private final int SIZE = 500;
	private Movie[] data;
	
	public NetflixHandler() {
		data = new Movie[SIZE];
	}
	
	public void read() {
		 Scanner input = null;
		
		try {
			int i =0;
			input = new Scanner(new File("netflix.cvs")).useDelimiter("[,\r\n]");
			
			while(input.hasNext()) {
				input.nextLine();
				String title = input.next();
				String rating = input.next();
				int year = Integer.parseInt(input.next());
				int score = Integer.parseInt(input.nextLine());
				Movie a = new Movie(title, rating, year, score);
				data[i] = a;
				i++;
			}
			input.close();
		}
		catch(FileNotFoundException e){
			System.out.println("File not found");
			System.exit(1);
		}
	}
	
	public void displayAllMovies() {
		for(int i = 0; i < actualSize; i++) {
			System.out.println(data[i].toString());
		}
	}
	
	public void searchTitle() {
		System.out.print("Please provide a title: ");
		String title = input.nextLine();
		String output = "";
		
		for(int i = 0; i < actualSize; i++) {
			if(title.equalsIgnoreCase(data[i].getTitle())) {
				output = data[i].toString();
				System.out.println(output);
			}
			else {
				output = "The title does not match any of the movies";
				System.out.println(output);
			}
		}
	}
	
	public void searchYear() {
		System.out.print("Please provide a year: ");
		int year = input.nextInt();
		String output = "";
		
		for(int i = 0; i < actualSize; i++) {
			if(year == (data[i].getYear())) {
				output = data[i].toString();
				System.out.println(output);
			}
			else {
				output = "The year does not match any of the movies";
				System.out.println(output);
			}
		}
	}
	
	public void sort(Movie[] movies, int size) {
		Movie temp;
		
		for(int i = 0; i < size - 1; i++) {
			
			for(int j = i+1; j < size; j++) {
				if(movies[j].getScore() > movies[i].getScore()) {
					temp = movies[j];
					movies[j] = movies[i];
					movies[i] = temp;
				}
			}
		}
		
	}
	
	public void makeRecommendations() {
		System.out.println("Do you want the recommendations based on ratings or score? \n1. Ratings \n2. scores \nPlease choose 1 or 2: ");
		int choice = input.nextInt();
		
		if(choice == 1) {
			sort(data, 5);
			int count = 0;
			
			PrintWriter pw = null;
			
			try {
				pw = new PrintWriter(new FileWriter("top_5_movies.txt"));
				
				while(count < 5) {
					pw.println(data[count]);
					count++;
				}
				
				
			}
			catch(IOException e) {
				e.printStackTrace();
			}
		}
		else if(choice ==2) {
			sort(data, 20);
			int count = 0;
			
			PrintWriter pw = null;
			
			try {
				pw = new PrintWriter(new FileWriter("top_20_movies.txt"));
				
				while(count < 20) {
					pw.println(data[count]);
					count++;
				}
			}
			catch(IOException e) {
				e.printStackTrace();
			}
		}
	}
	
}

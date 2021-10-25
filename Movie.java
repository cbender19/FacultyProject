/*
 * File name: Movie.java
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

/**
 * <insert class description here>
 *
 * @author Connor Bender
 *
 */
public class Movie
{
	private String title;
	private String rating;
	private int year;
	private int score;
	
	public Movie(String title, String rating, int year, int score) {
		this.title = title;
		this.rating = rating;
		this.year = year;
		this.score = score;
	}

	/**
	 * @return the title
	 */
	public String getTitle()
	{
		return title;
	}

	/**
	 * @return the rating
	 */
	public String getRating()
	{
		return rating;
	}

	/**
	 * @return the year
	 */
	public int getYear()
	{
		return year;
	}

	/**
	 * @return the score
	 */
	public int getScore()
	{
		return score;
	}
	
	public String toString() {
		return this.title +"\t" +this.year +"\t" +this.rating +"\t" +this.score;
	}
}

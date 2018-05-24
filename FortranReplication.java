import java.util.ArrayList;
import java.util.Scanner;

/*
 * Name: Michael Pedzimaz  
 * Class: Programming Languages
 * Assignment: #2, Question #3, Replicating the Fortran Code in Java
 */
public class FortranReplication {

	public static void main(String[] args) {
		int numQuantity;
		ArrayList<Integer> numbers = new ArrayList<Integer>();
		
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter amount of numbers you would like to calculate the sum and average of (Less than 100 please): ");
		numQuantity = sc.nextInt();
		if (numQuantity < 0 || numQuantity > 100){
			System.out.println("INCORRECT VALUE ENTERED, PROGRAM EXITTING!!");
			System.exit(0);
		}
		
		System.out.printf("Please enter a list of %d numbers, with the 'Enter' key pressed between each number: ", numQuantity);
		while (sc.hasNextInt()){
			int input = sc.nextInt();
			numbers.add(input);
			if ((numbers.size() > numQuantity) || (numbers.size() == numQuantity)){
				break;
			}
		}
		
		int sum = 0;
		for (int i: numbers){
			sum += i;
		}
		System.out.printf("Sum of numbers is %d.\n", sum);
		System.out.printf("Average of numbers is %d.", sum/numQuantity);
		
		
		
		//System.out.printf("The amount of numbers you want to add is %d", numQuantity);
		

	}

}

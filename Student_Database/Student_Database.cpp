/* Author: Michael Pedzimaz
								Program Name: Client-side Student Database		Version: 0.0.1
	This is a C++ program that ask the user to create students, stores them, then displays them out to the screen. 
	It utilizes a structure, various control statement schemes, and the use of multiple functions. 
	This program is part of a Microsoft Visual Studio "Solution", so it will not run unless the whole solution is imported into MVS and ran from there.
*/
#include "stdafx.h"
using namespace std;
// Structure declaration
struct student {
	string firstName;
	string lastName;
	int id;
}students[10];
// 'printStudents() function takes in two arguments, the established 'students[]' array & a student count number which signifies the amount of students the user inputted.
void printStudents(struct student students[], int studentC) {
	// for loop that iterates through each student and prints out his/her information to the console. 
	for (int i = 0; i < studentC; i++) {
		cout << students[i].firstName + " " << students[i].lastName + " " << "ID: " << students[i].id;
		cout << "\n";
	}
}
// main function 
int main() {
	/* variable declarations; 'answer'       : determines whether another student will be added
							  'printQuery'   : determines whether the user wants to print the students' information out
							  'studentCount' : determines how many students are actually in our structure object array
							  'index'        : iterates through 'students[]' and ensures a ceiling cap of students isn't surpassed.
	*/
	string answer;
	string printQuery;
	int studentCount = 0;
	int index = 0;	
	// Do-while loop runs as many times as the user chooses to add students. Contains a nested for loop that checks for conditions
	//  such as weather we have reached our max limit of student entries, or whether the user does not want to add any more students.
	do {
		cout << "Would you like to add a student? (Type 'Yes' or 'No'): ";
		getline(cin, answer);
		if (answer == "Yes") {
			// Add a new student to our student[] array
			if (index < 10) {
				cout << "Enter First Name: ";
				getline(cin, students[index].firstName);
				cout << "Enter Last Name: ";
				getline(cin, students[index].lastName);
				cout << "Enter ID No: ";
				cin >> students[index].id;
				cin.ignore();
				index = index + 1;
				studentCount = studentCount + 1;
			}
			else {
				cout << "\n";
				cout << "Sorry, the maximum amount of students has been entered." << endl;
				continue;
			}
		}
		else {
			cout << "Okay, no new students added." << endl;
		}
	} while (answer == "Yes");
	// Asking the user whether they would like to print their current list of students or not. 
	cout << "\n";
	cout << "Would you like to print out your list of students? (Type 'Yes' or 'No'): ";
	getline(cin, printQuery);
	// Checking for exact response, if 'Yes', program calls our secondary function to print out values. 
	if (printQuery == "Yes") {
		cout << "\n";
		printStudents(students, studentCount);
	}
	else {
		cout << "\n";
		cout << "Have a wonderful day.";
	}
	system("pause");
	return 0;
}




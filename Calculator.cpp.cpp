#include <iostream>
using namespace std;


struct  Mycalculator {void inputNumbers(double &number1, double &number2) {
    cout << "Enter the first real number: ";
    cin >> number1;
    cout << "Enter the second real number: ";
    cin >> number2;
}


double Theadditionfunction(double number1, double number2) {
    return number1 + number2;
}


double Thesubtractionfunction(double number1, double number2) {
    return number1 - number2;
}


double Themultiplicationfunction(double number1, double number2) {
    return number1 * number2;
}


double Thedivisionfunction(double number1, double number2) {
    if (number2 == 0) {
        cout << "OOPs.... Division by zero is Undefined, Please enter the correct devisor and try again.." << endl;
        return 0;
    }
    return number1 / number2;
}

};
int main() {
    Mycalculator calculator;
    cout<<"*******************************WELCOME TO THE CALCULATOR*************************************";
    int choice;
    double number1, number2, result;

    while (choice != 5) {
        
        cout << "\n\nHere is the Calculator Menu:" << endl;
        cout << "1. Addition" << endl;
        cout << "2. Subtraction" << endl;
        cout << "3. Multiplication" << endl;
        cout << "4. Division" << endl;
        cout << "5. Exit" << endl;
        cout << "Enter your choice (Please, choose from 1-5): ";
        cin >> choice;

        switch (choice) {
            case 1: 
                calculator.inputNumbers(number1, number2);
                result =calculator.Theadditionfunction(number1, number2);
                cout << "The Result of addition is::  " << result << endl;
                break;

            case 2:
                calculator.inputNumbers(number1,number2);
                result = calculator.Thesubtractionfunction(number1, number2);
                cout << "The result of subtraction is::  " << result << endl;
                break;

            case 3: 
                calculator.inputNumbers(number1,number2);
                result = calculator.Themultiplicationfunction(number1, number2);
                cout << "The Result of multiplication is::  " << result << endl;
                break;

            case 4: 
                calculator.inputNumbers(number1,number2);
                result = calculator.Thedivisionfunction(number1, number2);
                if (number2 != 0) {
                    cout << "The result of the division is::  " << result << endl;
                }
                break;

            case 5: 
                cout << "Exiting the program. Goodbye!" << endl;
                break;

            default: 
                cout << "OOps!....Please choose correctly from the given choices" << endl;
        }
    } 

    return 0;
}
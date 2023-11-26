#include <iostream>
using namespace std;

int main() {
    char option;
    char option1;
    float num1, num2;
    cout<<endl;
    	// Welcome message and  title
    cout << "\t\%%%%%%%%%%%%%%%%%" <<endl<<endl;
    cout << "\t CALCULATOR  " <<endl<<endl;
    cout << "\t*****************\t"  <<endl;
    cout << endl << endl;
    
	do {
        cout << "\tChoose Basic Operation From Below For Calculation:" << endl;
        cout << "\tEnter operator: +, -, *, /: ";
        cin >> option1; 
        cout << endl;
        cout << "\t*************" <<endl;
        cout << "\tEnter operand 1: ";
        cin >> num1;
        cout<<endl;
        cout << "\tEnter operand 2: ";
        cin >> num2;
        cout << endl;
        cout << "\t*************" <<endl;
        cout<<endl;
        cout << "\tResult displayed: ";
        switch (option1) {
            case '+':
                cout << num1 << " + " << num2 << " = " << num1 + num2;
                break;
            case '-':
                cout << num1 << " - " << num2 << " = " << num1 - num2;
                break;
            case '*':
                cout << num1 << " * " << num2 << " = " << num1 * num2;
                break;
            case '/':
                if (num2 != 0) {
                    cout << num1 << " / " << num2 << " = " << num1 / num2;
                } else {
                    cout << "Error! Division by zero is not allowed.";
                }
                break;
            default:
                cout << "Error! " << endl;
                break;
        }
        cout<<endl<<endl;
        cout << "\t************" ;
        cout << endl << endl;
        cout << "\tDo you want to continue? (y/n): ";
        cin >> option;
        cout << endl;

    } while (option == 'y' || option == 'Y');

      cout<<endl<<endl;
      cout << "\t\t\t\t*************" ;
      cout <<endl<<endl<< "\t\t\tThanks for visiting!" << endl;
      cout<<endl<<endl;
      cout << "\t\t\t\t*************" ;
    return 0;
}

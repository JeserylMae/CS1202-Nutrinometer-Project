/*
Create a program that have the following output:
    a. average
    b. largest
    c. smallest
    d. exit

    Choose a letter:
*/

#include <iostream>
#include <string>

void loop();

int main(){

    // menu header
    std::string menu_h = "\na. average \nb. largest \nc. smallest \nd. exit\n";

    // prompt
    char ch; 
    std::cout << menu_h << "\nChoose a letter:\t";
    std::cin >> ch;

    int num1, num2, num3, num4, num5, num6, num7, num8, num9, num10;

    // menu directory
    switch (ch) {
        case 'a':
        case 'A':
            // prompt user to enter numbers.
            std::cout << "\nEnter 10 Numbers:\n";
            std::cin >> num1 >> num2 >> num3 >> num4 >> num5 >> num6 >> num7 >> num8 >> num9 >> num10;

            float sum, ave;
            sum = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10;
            ave = sum / 10;

            std::cout << "\nAverage:\t" << ave;
            loop();
            break;

        case 'b':
        case 'B':
            // prompt user to enter numbers.
            int num_l[10];
            for (int i = 0; i < 10; i++) {
                std::cout << "Number " << i+1 << ":\t";
                std::cin >> num_l[i];
            }

            int largest;
            largest = num_l[9];
            // determining the smallest number.
            for (int i = 0; i < 10; i++) {
                if (largest < num_l[i]) {
                    largest = num_l[i];
                }
            } std::cout << "\nLargest:\t" << largest;

            loop();
            break;

        case 'c':
        case 'C':
            // prompt user to enter numbers.
            int num[10];
            for (int i = 0; i < 10; i++) {
                std::cout << "Number " << i+1 << ":\t";
                std::cin >> num[i];
            }

            int smallest;
            smallest = num[9];
            // determining the smallest number.
            for (int i = 8; i >= 0; i--) {
                if (smallest > num[i]) {
                    smallest = num[i];
                }
            } std::cout << "\nSmallest:\t" << smallest;

            loop();
            break;  

        case 'd':
        case 'D':
            exit(0);
            break;

        default:
            break;
        }
        
    return 0;
}

void loop(){
    int ch;
    std::cout << "\n[1] Again\t\t[0] Exit\nChoice:\t";
    std::cin >> ch;

    if (ch == 1){
        system("cls");
        main();
    } else{
        exit(0);
    }
}
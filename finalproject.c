#include <cs50.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>

#define SIZE1 5000
#define SIZE2 10000
#define SIZE3 50000
int *readFile(string fileName, int size, int size2);  //pointer to return and int array
int linearSearch(int array[], int guess, int size);  //linear search
int binarySearch(int array[], int guess, int size);
int *bubbleSort(int array[], int size);
int *selectionSort(int array[], int size);
void printArray(int array[], int size);
void writeArray(int array[], int size);
void menu();


int main(void)
{
    int choice = 0;
    int *sorted;
    int *array;
    int size=0;
    do{
    menu();
    choice = get_int ("Selection an option from 1 to 5: ");
    string fileName=" ";
    switch (choice)
    {
            bool check = false;
            case 1:
                size = get_int("Choose the size of the file (5000, 10000, or 50000):\n");
                check = true;
                do
                {
                if (size==5000)
                {
                    size = 5000;
                }
                else if (size==10000)
                {
                    size= 10000;
                }
                else
                {
                    size = 50000;
                }
                } while (size!=5000&&size!=10000&&size!=50000);

                fileName=get_string("Enter File name: ");
                FILE* file=(fopen(fileName, "r"));
                if(!file)
                {
                printf("\n Unable to open: %s ", fileName);
                return -1;
                }
                fclose(file);
                array=readFile(fileName, size, 5);   // call of the read function
                break;

            case 2:
            if (check==true)
            {
                printf("1. Bubble Sort\n");
                printf("2. Selection Sort\n");
                choice = get_int ("Enter your choice (1 or 2): ");


                    if (choice == 1)
                    {
                        sorted = bubbleSort(array, size);
                        printf("Array sorted using Bubble Sort.\n");
                    }
                    else if (choice == 2)
                    {
                        sorted = selectionSort(array, size);
                        printf("Array sorted using Selection Sort.\n");
                    }
                    else
                    {
                        printf("Invalid sort choice.\n");
                        continue; // Restart the loop
                    }
            }
            else
            {
                printf("You need to create your file first (selection 1)");
            }
                break;
            case 3:
            if (check==true)
            {
                printf("1. Linear Search\n");
                printf("2. Binary Search\n");
                choice = get_int("Enter your choice (1 or 2): ");
                int guess=get_int("give me a number in between 1 - %i ", size);
                if (choice == 1)
                    {
                        int indx = linearSearch(array, guess, size); // call of the search function
                        printf("the index is %i \n", indx);
                    }
                    else if (choice == 2)
                    {

                        int indx = binarySearch(array, guess, size); // call of the search function
                        printf("the index is %i \n", indx);
                    }
                    else
                    {
                        printf("Invalid search choice.\n");
                        continue; // Restart the loop
                    }
            }
            else
            {
                printf("You need to create your file first (selection 1)");
            }
                break;
            case 4:
            if (check==true)
            {
                printf("1. Print Array\n");
                printf("2. Write Array\n");
                choice = get_int("Enter your choice (1 or 2): ");
                if (choice == 1)
                    {
                        printArray(sorted, size);
                    }
                    else if (choice == 2)
                    {
                        writeArray(sorted, size);
                    }
                    else
                    {
                        printf("Invalid sort choice.\n");
                        continue; // Restart the loop
                    }
            }

            else
            {
                printf("You need to create your file first (selection 1)");
            }
                break;
            case 5:
                printf("Quitting the program. Goodbye!\n");
                break;
            default:
                printf("Invalid choice. Please enter a number between 1 and 5.\n");
    }
    }while (choice!=5);
    }


void menu()
{
    printf("\nMenu:\n");
    printf("1. Read a file\n");
    printf("2. Sort an array\n");
    printf("3. Search for a value in array\n");
    printf("4. Print or write a file\n");
    printf("5. Exit\n");
}

int* readFile(string fileName, int size, int size2)
{
    FILE* file = fopen(fileName, "r");

    char line[size2];
    char options[size][size2];

    int* numbers = (int*)malloc(size * sizeof(int)); // Dynamically allocate memory

    for (int i = 0; i < size; i++) {
        if (fscanf(file, "%s", options[i]) != 1) {
            // Handle fscanf error
            free(numbers); // Free allocated memory
            fclose(file);
        }
        numbers[i] = atoi(options[i]);
    }
    fclose(file);
    return numbers;
}

int linearSearch(int array[],int guess, int size)
{
    for(int i=0; i < size; i++)
    {
        if (array[i]==guess)
        {
            return i;
        }
    }
    return -1;
}
int binarySearch(int array[], int guess, int size)
{
    char options [size][5];
   for (int i = 0; i<size; i++)
    {
        int n = atoi(options[i/2]);
        int k = i/2;
        if(n==guess)
        {
            return k;
        }
    }
    return -1;
}
int *bubbleSort(int array[], int size)
{
    for (int i = 0; i < size; i++)
    {
        int j = i+1;
        for (i =0; i < size; i++)
        {
            if (array[i]>array[j])
            {
            int temp = array[i];
            array[i] = array[j];
            array[j] = temp;
            }
        }
    }
    return array;
}

int *selectionSort(int array[], int size)
{
    int indx = 0;
    for(int i =0; i<size; i++)
    {
        int min = size+1;
        for(int j=i; j<size; j++)
        {
            if (array [j]<min)
            {
                min = array[j];
                indx=j;
            }
        }
        int temp = array [i];
        array[i]=min;
        array[indx]=temp;
    }
    return array;
}
void printArray(int array[], int size)
{
    for (int i =0; i<size; i++)
    {
        printf("%i \n", array[i]);
    }

}
void writeArray(int array[], int size)
{
    string nameoffile = get_string("Name a file to store the sorted array: ");
    char wfilename[12];
    sprintf(wfilename, "%s.txt", nameoffile);
    FILE *myThings = fopen(wfilename, "w");
    for (int i =0; i<size; i++)
    {
        printf("%i \n", array[i]);
        fprintf(myThings,"%d\n", array[i]);
    }
    fclose(myThings);
}


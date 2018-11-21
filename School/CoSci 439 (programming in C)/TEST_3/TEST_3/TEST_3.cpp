//	Aaron Alvarado
//	CoSci 439
//	Test 2
// the flight itinerary program for test 3

#include "stdafx.h"
#include <iostream>
using namespace System;
using namespace std;
int flight1[15], flight2[15], flight3[15]; //stores seats and class taken
char nmLst1[15][100], nmLst2[15][100], nmLst3[15][100]; //stores names for corresponding flights
int x = 0;
int y = 0;
int frontpage(int srvc);
int flightbook(int srvc);
void listings(int flight1[], int flight2[], int flight3[], int x);
void bookflight1(int flight1[], int x, char nmLst1[15][100]);
void bookflight2(int flight2[], int x, char nmLst2[15][100]);
void bookflight3(int flight3[], int x, char nmLst3[15][100]);
void cls(int flight1[], int flight2[], int flight3[], int x);
void custLst(int flight1[], int flight2[], int flight3[], int x, char nmLst1[15][100], char nmLst2[15][100], char nmLst3[15][100]);
int main()
{
	int srvc = 0;
	//fill arrays
	for (x = 0; x<15; x++)
	{
		flight1[x] = 0;
		flight2[x] = 0;
		flight3[x] = 0;
	}
	srvc = frontpage(srvc);
	while (srvc != 4) //keeps the program looping until the user quits
	{
		if (srvc == 1) //the beggining of the booking proccess 
		{
			int flightNum;
			printf("\nwhich flight would you like to take?\n\nNUMBER\tDAY\tTIME\n"); //defining which flight they want to book on
			printf("1\t Mon \t 6:00 AM \n");
			printf("2\t Wed \t 12:00 PM \n");
			printf("3\t Fri \t 6:00 PM \n");
			scanf("%d", &flightNum);
			if (flightNum == 1)
			{
				bookflight1(flight1, x, nmLst1); //booking for flight 1
			}
			if (flightNum == 2)
			{
				bookflight2(flight2, x, nmLst2); //booking for flight 2
			}
			if (flightNum == 3)
			{
				bookflight3(flight3, x, nmLst3); //booking for flight 3
			}
		}
		if (srvc == 2) //show current listing and seats taken
			listings(flight1, flight2, flight3, x);
		if (srvc == 3)
		{
			custLst(flight1, flight2, flight3, x, nmLst1, nmLst2, nmLst3);
		}
		system("cls");
		srvc = frontpage(srvc); //loops back around to beggining
	}
	return 0;
}



////displays front page
int frontpage(int srvc)
{
	printf("------------------------------------------\n");
	printf("\t* FAST FLIGHT AIRLINES *\n");
	printf("------------------------------------------\n");
	printf("\t     FLIGHT SCHEDULE\n");
	printf("------------------------------------------\n");
	printf("\tNUMBER\tDAY\tTIME\n");
	printf("\t1\t Mon \t 6:00 AM \n");
	printf("\t2\t Wed \t 12:00 PM \n");
	printf("\t3\t Fri \t 6:00 PM \n");
	printf("------------------------------------------\n");
	printf("What would you like to do today?\n1 = Book a flight\n2 = Seats available\n3 = Customer Listings\n4 = Quit\n");
	scanf(" %d", &srvc);
	return srvc;
}



////prints out seat avialability for each flight
void listings(int flight1[], int flight2[], int flight3[], int x)
{
	int total1 = 15, total2 = 15, total3 = 15, seat1, seat2, seat3, choice;
	x = 0;
	for (x=0; x <15; x++) //checks each seat in order for all 3 flight for aviability
	{
		if (flight1[x] == 1 || flight1[x] == 2)
			seat1++;
		if (flight2[x] == 1 || flight2[x] == 2)
			seat2++;
		if (flight3[x] == 1 || flight3[x] == 2)
			seat3++;	
	}
	total1 = 15 - seat1;
	total2 = 15 - seat2;
	total3 = 15 - seat3;
	printf("%d seats aviable on flight 1\n", total1);
	printf("%d seats aviable on flight 2\n", total2);
	printf("%d seats aviable on flight 3\n", total3);
	printf("would you like to see which seats are taken?\n1 = yes\n2 = no\n");
	scanf("%d", &choice);
	if (choice == 1)
		cls(flight1, flight2, flight3, x);
	system("pause");
}


//////booking a seat on flight one
void bookflight1(int flight1[], int x, char nmLst1[15][100])
{
	x = 0;
	printf("bookings for flight 1\n");
	while ( flight1[x] == 1 || flight1[x] == 2)
		x++;
	if( x < 15) //makes sure flight isn't full before booking
	{
		printf("please select a class\n1 = First Class\n2 = Coach\n0 = Cancel order\n");
		scanf("%d", &flight1[x]);
		if (flight1[x] != 0)
		{
			printf("enter your name:");
			scanf("%100s", nmLst1[x]);
			system("cls");
			printf("\t**Here is your itinerary**\n\t   **enjoy your flight**\n");
			if (x == 1) //prints itinerary
				printf("Name: %s\nSeat Number: %d\nFlight 1\nFirst Class\nTime of departure: Monday 6:00 AM\n\nplease print this out and bring to gate\n", nmLst1[x], x);
			else
				printf("Name: %s\nSeat Number: %d\nFlight 1\nCoach\nTime of departure: Monday 6:00 AM\n\nplease print this out and bring to gate\n", nmLst1[x], x);
		}
	}
	else
		printf("sorry but this flight is full\n");
	system("pause");
}


////Booking a seat on flight 2
void bookflight2(int flight2[], int x, char nmLst2[15][100])
{
	x = 0;
	printf("bookings for flight 2\n");
	while ( flight2[x] == 1 || flight2[x] == 2)
		x++;
	if( x < 15) //makes sure flight isn't full before booking
	{
		printf("please select a class\n1 = First Class\n2 = Coach\n0 = Cancel order\n");
		scanf("%d", &flight2[x]);
		if (flight1[x] != 0)
		{
			printf("enter your name:");
			scanf("%100s", nmLst2[x]);
			system("cls");
			printf("\t**Here is your itinerary**\n\t   **enjoy your flight**\n");
			if (x == 1) //prints itinerary
				printf("Name: %s\nSeat Number: %d\nFlight 2\nFirst Class\nTime of departure: Wednesday 12:00 PM\n\nplease print this out and bring to gate\n", nmLst2[x], x);
			else
				printf("Name: %s\nSeat Number: %d\nFlight 2\nCoach\nTime of departure: Wednesday 12:00 PM\n\nplease print this out and bring to gate\n", nmLst2[x], x);
			/*name = nmLst1[x];*/
		}
	}
	else
		printf("sorry but this flight is full\n");
	system("pause");
}


////booking a seat on flight 3
void bookflight3(int flight3[], int x, char nmLst3[15][100])
{
	x = 0;
	printf("bookings for flight 3\n");
	while ( flight3[x] == 1 || flight3[x] == 2)
		x++;
	if( x < 15) //makes sure flight isn't full before booking
	{
		printf("please select a class\n1 = First Class\n2 = Coach\n0 = Cancel order\n");
		scanf("%d", &flight3[x]);
		if (flight1[x] != 0)
		{
			printf("enter your name:");
			scanf("%100s", nmLst3[x]);
			system("cls");
			printf("\t**Here is your itinerary**\n\t   **enjoy your flight**\n");
			if (x == 1) //prints itinerary
				printf("Name: %s\nSeat Number: %d\nFlight 3\nFirst Class\nTime of departure: Friday 6:00 PM\n\nplease print this out and bring to gate\n", nmLst3[x], x);
			else
				printf("Name: %s\nSeat Number: %d\nFlight 3\nCoach\nTime of departure: Friday 6:00 PM\n\nplease print this out and bring to gate\n", nmLst3[x], x);
			/*name = nmLst1[x];*/
		}
	}
	else
		printf("sorry but this flight is full\n");
	system("pause");
}


//prints what seats are taken
void cls(int flight1[], int flight2[], int flight3[], int x)
{
	int coach1=0, coach2=0, coach3=0, first1=0, first2=0, first3=0;
	for (x=0; x <15; x++)
	{
		if (flight1[x] == 2)
			first1++;
		if (flight1[x] == 1)
			coach1++;
		if (flight2[x] == 2)
			first2++;
		if (flight2[x] == 1)
			coach2++;
		if (flight3[x] == 2)
			first3++;
		if (flight3[x] == 1)
			coach3++;
	}
	printf("\n%d coach and %d first class taken in flight 1", coach1, first1);
	printf("\n%d coach and %d first class taken in flight 2", coach2, first2);
	printf("\n%d coach and %d first class taken in flight 3\n", coach3, first3);
}


//shows customer names and corresponding seat and flight
void custLst(int flight1[], int flight2[], int flight3[], int x, char nmLst1[15][100], char nmLst2[15][100], char nmLst3[15][100])
{
	system("cls");
	printf("\t***Flight 1***\n");
	for (x=0; x<15; x++)
	{
		if ((nmLst1[x] != 0)&&(flight1[x] != 0)) //checks to make sure it won't print a empty seat
			printf("Name: %s\tseat: %d\n", nmLst1[x], flight1[x]);
	}
	printf("\t***Flight 2***\n");
	for (x=0; x<15; x++)
	{
		if ((nmLst2[x] != 0)&&(flight2[x] != 0))
			printf("Name: %s\tseat: %d\n", nmLst2[x], flight2[x]);
	}
	printf("\t***Flight 3***\n");
	for (x=0; x<15; x++)
	{
		if ((nmLst3[x] != 0)&&(flight3[x] != 0))
			printf("Name: %s\tseat: %d\n", nmLst3[x], flight3[x]);
	}
	system("pause");
}
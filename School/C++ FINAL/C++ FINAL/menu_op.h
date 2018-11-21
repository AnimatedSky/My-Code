#ifndef MENU_OP_H
#define MENU_OP_H
#include "stdafx.h"
#include <string>
#include <iostream>
#include <fstream>
using namespace std;
using namespace System;

struct waiting
{
	string fname;
	string lname;
	char smoke;
	int row;
	int column;
};
struct pass
{
	string fname;
	string lname;
	bool taken;
};
pass smoking[4][4], nonsmoking[4][8];
waiting list[100], entry;
int code = 12345, psent, count;
ifstream inFile;
ofstream outFile;




int mainmenu()
{
	int menu;
	cout << "Hello and welcome to the Fast Flight Alrines booking software.\nPlease select from one of our following options" << endl;
	cout << "1. view current listings\t\t2. print current listings" << endl;
	cout << "3. reserve seating\t\t\t4. alter current listing(admin)" << endl;
	cout << "5. quit" << endl;
	cin >> menu;
	system("cls");
	return menu;
}


void menu1(pass smoking[4][4], pass nonsmoking[4][8], waiting list[100], int count) // view current listings
{
	cout <<"\n****************************************************************************************************" << endl;
	cout <<"*" << endl;
	cout <<"*\t\t\tNON SMOKING SECTION" << endl;
	cout <<"*" << endl;
	cout <<"****************************************************************************************************" << endl << endl;
	for(int x=1; x<8; x++)
		cout <<nonsmoking[1][x].fname<<" "<<nonsmoking[1][x].lname<<"\t\t"<<nonsmoking[2][x].fname<<" "<<nonsmoking[2][x].lname<<"\t\t"<<nonsmoking[3][x].fname<<" "<<nonsmoking[3][x].lname<<endl;
	cout <<"****************************************************************************************************" << endl;
	cout <<"*" << endl;
	cout <<"*\t\t\tSMOKING SECTION" << endl;
	cout <<"*" << endl;
	cout <<"****************************************************************************************************" << endl << endl;
	for(int x=1; x<4; x++)
		cout <<smoking[1][x].fname<<" "<<nonsmoking[1][x].lname<<"\t\t"<<nonsmoking[2][x].fname<<" "<<nonsmoking[2][x].lname<<"\t\t"<<nonsmoking[3][x].fname<<" "<<nonsmoking[3][x].lname<<endl;
	cout <<"****************************************************************************************************" << endl;
	cout <<"*" << endl;
	cout <<"*\t\t\tWAITING LIST" << endl;
	cout <<"*" << endl;
	cout <<"****************************************************************************************************" << endl << endl;
	cout <<"Name\t\t\tsmoke\trow\tcolumn\n";
	for(int x=0; x<count; x++)
	{
		cout << list[x].fname<<" "<< list[x].lname<<"\t\t"<<list[x].smoke <<"\t"<<list[x].row <<"\t"<<list[x].column << endl;
	}
	cout <<"****************************************************************************************************" << endl;
	system("pause");
}

void menu2(ofstream & outFile, pass smoking[4][4], pass nonsmoking[4][8],waiting list[100], int count) // print current listings
{
	outFile.open("full_list.txt");
	outFile <<"name\t\t\tsmoke\trow\tcolumn" << endl;
	for(int x=1; x<=7; x++)
	{
		for(int y=1; y<=3; y++)
			outFile <<"\n"<<nonsmoking[y][x].fname<<" "<<nonsmoking[y][x].lname<<"\t\tn\t"<<y<<"\t"<<x;
	}
	for(int x=1; x<=3; x++)
	{
		for(int y=1; y<=3; y++)
			outFile <<"\n"<<smoking[y][x].fname<<" "<<nonsmoking[y][x].lname<<"\t\ts\t"<<y<<"\t"<<x;
	}
	for(int x=0; x<count; x++)
	{
		outFile <<"\n"<<list[x].fname<<" "<< list[x].lname<<"\t\t"<<list[x].smoke <<"\t"<<list[x].row <<"\t"<<list[x].column;
	}
	system("pause");
}

void menu3(ifstream & inFile, ofstream & outFile, pass smoking[4][4], pass nonsmoking[4][8], waiting list[100], waiting entry, int count) // reserve seating
{
	cout << "Will this be smoking or nonsmoking(s = smoking, n = nonsmoking)" << endl;
	cin	>> entry.smoke;
	cout << "\nPlease enter your first name: ";
	cin >> entry.fname;
	cout << "\nPlease enter your last name: ";
	cin >> entry.lname;
	cout << "Where would you like to sit?" << endl;
	cout << "row: ";
	cin >> entry.row;
	cout << "column: ";
	cin >> entry.column;
	if (entry.smoke == 's')
	{
		if (smoking[entry.column][entry.row].taken == false)
		{
			outFile.open("write.txt", ios::app);
			outFile <<"\n"<< entry.lname << " " << entry.fname <<"\t\t"<< entry.smoke <<"\t"<< entry.row<<"\t"<<entry.column;
			outFile.close();
			smoking[entry.row][entry.column].taken = true;
			cout << "\nyour seat has been succesfully reserved" << endl;
		}
		else
		{
			outFile.open("list.txt", ios::app);
			outFile <<"\n"<< entry.lname << " " << entry.fname <<"\t\t"<< entry.smoke <<"\t"<< entry.row<<"\t"<<entry.column;
			outFile.close();
			cout << "\nsorry that seat is taken you will be put on the waiting list" << endl;
		}
	}
	if (entry.smoke == 'n')
	{
		if (nonsmoking[entry.row][entry.column].taken == false)
		{
			outFile.open("write.txt", ios::app);
			outFile <<"\n"<< entry.lname << " " << entry.fname <<"\t\t"<< entry.smoke <<"\t"<< entry.row<<"\t"<<entry.column;
			outFile.close();
			nonsmoking[entry.row][entry.column].taken = true;
			cout << "\nyour seat has been succesfully reserved" << endl;
		}
		else
		{
			outFile.open("list.txt", ios::app);
			outFile <<"\n"<< entry.lname << " " << entry.fname <<"\t\t"<< entry.smoke <<"\t"<< entry.row<<"\t"<<entry.column;
			outFile.close();
			cout << "\nsorry that seat is taken you will be put on the waiting list" << endl;
			entry.fname = list[count++].fname;
			entry.lname = list[count++].lname;
			entry.smoke = list[count++].smoke;
			entry.fname = list[count++].fname;
			entry.row = list[count++].row;
			entry.column = list[count++].column;
		}
	}
	system("pause");
}

void menu4(int code,int psent, pass smoking[4][4], pass nonsmoking[4][8], waiting list[100], waiting entry) // alter current listing(admin)
{
	cout << "Please enter the password:";
	cin >> psent;
	if(psent == code)
	{
		cout << "how many seats will you alter?\n";
		int seat;
		cin >> seat;
		for(int x = 0; x<=seat; x++);
		{
			cout << "what seat will you like to alter?\n";
			cout << "row: ";
			cin >> entry.row;
			cout << "column: ";
			cin >> entry.column;
			cout << "smoking or non-smoking(s = smoking, n = nonsmoking)" << endl;
			cin >> entry.smoke;
			cout <<"are you sure you want to clear this seat?(0 = no, 1 = yes)\n";
			int ans;
			cin >> ans;
			if(ans == 1)
			{
				if (entry.smoke == 's')
					smoking[entry.column][entry.row].taken = false;
				else
					nonsmoking[entry.column][entry.row].taken = false;
			}
		}
	}
	else
		cout << "invalid password";
	system("pause");
}

void Populate(ifstream & inFile, ofstream & outFile, pass smoking[4][4], pass nonsmoking[4][8], waiting list[100], waiting entry, int count)
{
		inFile.open("write.txt");
		while(!inFile.eof())
		{
			inFile >> entry.lname >> entry.fname >> entry.smoke >> entry.row >> entry.column;
			if (entry.smoke == 's')
			{
				smoking[entry.row][entry.column].fname = entry.fname;
				smoking[entry.row][entry.column].lname = entry.lname;
				smoking[entry.row][entry.column].taken = true;
			}
			if (entry.smoke == 'n')
			{
				nonsmoking[entry.row][entry.column].fname = entry.fname;
				nonsmoking[entry.row][entry.column].lname = entry.lname;
				nonsmoking[entry.row][entry.column].taken = true;
			}
		}
		inFile.close();
		inFile.open("list.txt");
		count = 0;
		while(!inFile.eof())
		{
			inFile >> list[count].lname >> list[count].fname >> list[count].smoke >> list[count].row >> list[count].column;
			count++;
		}
		inFile.close();
}
void fill(pass smoking[4][4],pass nonsmoking[4][8])
{
	for(int x=1; x<=7; x++)
	{
		for(int y=1; y<=3; y++)
		{
			nonsmoking[y][x].fname = "free";
			nonsmoking[y][x].lname = "space";
			nonsmoking[y][x].taken = false;
		}
	}
	for(int x=1; x<=3; x++)
	{
		for(int y=1; y<=3; y++)
		{
			smoking[y][x].fname = "free";
			smoking[y][x].lname = "space";
			smoking[y][x].taken = false;
		}
	}

}
#endif
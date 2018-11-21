//	Aaron Alvarado
//	CoSci 440
//	c final

#include "stdafx.h"
#include "menu_op.h"
#include <iostream>
#include <string>
#include <fstream>
using namespace System;
using namespace std;
//struct waiting
//{
//	string fname;
//	string lname;
//	char smoke;
//	int row;
//	int column;
//};
//struct pass
//{
//	string fname;
//	string lname;
//	bool taken; //use to track if a seat is filled (more reliable then checking the name)
//};

int main()
{
	fill(smoking, nonsmoking);
	int mmenu = mainmenu();
	while (mmenu != 5)
	{
		Populate(inFile, outFile, smoking, nonsmoking, list, entry, count);
		switch (mmenu)
		{
		case 1: //view current listings
		{
			menu1(smoking, nonsmoking, list, count);
			break;
		}
		case 2: // print current listings
		{
			menu2(outFile, smoking, nonsmoking, list, count);
			/*outFile.open("full_list.txt");
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
			system("pause");*/
			break;
		}
		case 3:  // reserve seating
		{
			menu3(inFile, outFile, smoking, nonsmoking, list, entry, count);
			/*cout << "Will this be smoking or nonsmoking(s = smoking, n = nonsmoking)" << endl;
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
				}
			}
			system("pause");*/
			break;
		}
		case 4: //alter current listing(admin)
			{
				menu4(code, psent, smoking, nonsmoking, list, entry);
				/*cout << "Please enter the password:";
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
				break;*/
			}
		default:
			{
			cout << "invalid input, please try again" << endl;
			system("pause");
			break;
			}
		}
		system("cls");
		mmenu = mainmenu();
	}
	cout << "\ndone\n";
	system("pause");
}
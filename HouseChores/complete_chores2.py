#!/bin/python3

from room import HouseChores
import os
import sys

def main():

    file = [sys.argv[1]]
    file_name = "house_chores2.txt"
    timetable = HouseChores(file)
    new_timetable = input("Enter the name of the file to store the new timetable: ")
    timetable.write_to_file(new_timetable)
    return

main()

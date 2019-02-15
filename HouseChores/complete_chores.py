#!/bin/python3

from room import HouseChores
import os
import sys

def main():

    file = sys.argv[1]
    timetable = HouseChores(file)
    # new_timetable = input("Enter the name of the file to store the new timetable: ")
    timetable.read_file()
    print("Writing to file...")
    timetable.write_to_file()
    print("Finishing up..")
    print("Done")
    return

main()

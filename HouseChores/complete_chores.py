#!/bin/python3

from room import HouseChores
import os

def main():

    file = "2HouseChores.xlsx"
    file_name = "house_chores2.txt"
    timetable = HouseChores(file)

    if file_name in os.listdir():
        # this is not the first time running the script
        timetable.read_file()
        timetable.write_to_file()
    else:
        new_members = first_time(file_name)
        timetable.first_timetable(new_members)
    print("Found the file reference")
    return

def first_time(file_name):
    '''Create a file containing room details having run
       the timetable for the first time'''

    new_members=dict()
    while True:
        room_member = input("Enter room member: ").lower().capitalize()
        if room_member:
            email_address = input("Enter %s's email address: " %(room_member))
            new_members[room_member] = email_address
        else:
            break
    # write to file house_chores
    file = open(file_name,'w')
    for k,v in new_members.items():
        file.write(k+':'+v)
        file.write('\n')
    file.close()
    print("Your file has been written")

    return new_members

main()

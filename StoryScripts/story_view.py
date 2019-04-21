#!/bin/python

from tkinter import *


class Application(Frame):
    """Create GUI for story program."""
    def __init__(self):
        """Initialize frame."""
        super(Application, self).__init__(master)
        self.grid()  # make gui visible
        self.create_widgets()

    def create_widgets(self):
        """Create labels,text entry and radio buttons"""
        pass

    def reveal(self):
        """Display the story after submission"""
        pass

    def save(self):
        """Give an option to save the story to the users PC."""
        pass


def main():
    """Interact with the GUI class and have window."""
    root = Tk()
    root.title("Story Mania")
    root.geometry("300x200")

    app = Application(root)
    root.mainloop()
    return


if __name__ == '__main__':
    main()

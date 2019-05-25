#!/bin/python3

from tkinter import *
from tkinter import filedialog
from StoryScripts.story_sources import NewStory

# global instance
user = NewStory()


class StoryMania(Frame):
    """Create a narrative."""

    def __init__(self, master):
        """Initialize frame."""
        super(StoryMania, self).__init__(master)
        self.grid()  # make visible widgets
        self.create_widgets()

    def create_widgets(self):
        """Create label,text entry and display for story."""
        Label(self, text="Choose a genre:").grid(row=0, column=0, sticky=W)
        # create variable for single genre
        self.genre = StringVar()
        self.genre.set(None)
        # create radio button for category
        category = ["Adventure", "Epic", "Thriller"]
        column = 1
        for item in category:
            Radiobutton(self, text=item, variable=self.genre, value=item).grid(row=1, column=column, sticky=W)
            column += 1
        # create label and text entries for character names
        Label(self, text="Character: ").grid(row=4, column=0, sticky=W)
        self.character = Entry(self)
        self.character.grid(row=5, column=0)
        # create submit buttons
        self.submit = Button(self, text="Submit", command=self.reveal)
        self.submit.grid(row=6,column=0)
        # text widget to display story
        self.narrative = Text(self, width=50, height=25, wrap=WORD)
        # self.narrative.pack()
        self.narrative.grid(row=7, column=0, columnspan=3, sticky=W)
        # create save button
        self.savefile = Button(self, text="Save story", command=self.save_file)
        self.savefile.grid(row=8, column=0)

    def save_file(self):
        """Update narrative given genre."""
        self.name = filedialog.asksaveasfile()


    def reveal(self):
        """Display results of story after submission."""
        story = self.genre.get()
        character = self.character.get()
        # output_file = user.get_information(story, character)
        output_file = '../Programfiles/Intermediates/intermediate.txt'
        self.narrative.delete(0.0, END)
        # with open(output_file,'r') as reader:
        #    display = reader.read()
        # text.insert('end', open(filename, 'r').read())
        self.narrative.insert(END,open(output_file,'r').read())



def main():
    """Interact with class."""
    root = Tk()
    root.title("StoryMania")
    # root.geometry("300x300")

    app = StoryMania(root)
    root.mainloop()


if __name__ == '__main__':
    main()

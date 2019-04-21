#!/bin/python3

from tkinter import *
from StoryScripts.story_sources import NewStory

# global instance
user = NewStory()

class StoryMania(Frame):
    """Create a narrative"""
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
        category = ["Adventure", "Romance", "Thriller"]
        column = 1
        for item in category:
            Radiobutton(self, text=item, variable=self.genre, value=item, command=self.update_txt).grid(row=1,column=column,sticky=W)
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
        self.narrative.grid(row=7, column=0, columnspan=3, sticky=W)

    def update_txt(self):
        """Update narrative given genre."""
        pass

    def reveal(self):
        """Display results of story after submission."""
        story = self.genre.get()
        character = self.character.get()
        self.narrative.delete(0.0, END)
        self.narrative.insert(0.0, story)
        pass


def main():
    """interact with class"""
    root = Tk()
    root.title("StoryMania")
    # root.geometry("300x300")

    app = StoryMania(root)
    root.mainloop()


if __name__ == '__main__':
    main()

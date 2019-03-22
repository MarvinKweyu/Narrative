#takes user input,changes content in an existing file
# to match input and makes a new file of it saving it as a pdf and displaying it with
# an option to send to the otehr game participants

import PyPDF2

class Application(object):
    'This is for a story'

    def __init__(self,play_file):
        self.play_file = play_file
        self.get_information()

    def get_information(self):
        '''Open the text file ,edit and write edited work to a new file.
        Code works without dictionary'''
        self.replacement_words = {'chicken':'goose',
                             'Marvin':'Kweyu',
                             'Melvin':'Emmanuel'
                            }

        self.file = open(self.play_file,'r')

        self.content = self.file.read()
        self.new_output_file = open('2'+self.play_file,'w')
        # for word in self.content:
        #     # print(word)
        #     if word in self.replacement_words:
        #         word = self.replacement_words[word]
        # print(self.content)
            # self.new_content.append(word)
        self.new_output_file.write(str(self.new_content))
        self.new_output_file.write(self.content.replace('chicken','goose'))
        # self.display()
        print("Your file has been written successfully")

    def display(self):
        'Show the information to user'
        pass

    def convert_to_pdf(self):
        ''
        pass

#main
def main():
    print(__file__ + 'new way')
    # internal_file = 'Story.txt'
    # new_user = Application(internal_file)
    return
main()

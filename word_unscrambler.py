#Strips and lowers the user input, checks if the input is null or "", and checks if the input is in word list
def validate_input(user_input, word_list = None):
    user_input = user_input.strip().lower()
    if user_input != None and user_input != "":
        if word_list != None:
            if user_input in word_list:
                return True
            else:
                print("Word does not exist")    
                return False
        return True
    else:
        print("Please enter something")
        return False

#checks if the input's letters are in the base letters
def is_word_in_base(word_entry, base_letters):
    holder = base_letters.copy()
    for letter in word_entry:
        if letter in holder:
            holder.remove(letter)
        else:
            return False
    return True

###################
#Reads the file and sorts it into lines
f = open('words.txt')
data = f.readlines()

#strips and standardizes the words.txt
for i in range(0,len(data)):
    data[i] = data[i].strip().lower()
#Main Loop
interupt = False
while not interupt:
    user_input = input("Please enter a word: ")
    user_input = user_input.lower()
    #Allows the user to exit the program 
    if user_input == "q":
        interupt = True
    else:
        #User Input, sorts the letters in alphanumeric order
        validate_input(user_input,data)
        input_letters = sorted(user_input)

        #Creating lists to store the words in
        six_letter = []
        five_letter = []
        four_letter = []
        three_letter = []   
        #Looping through the data set, testing each word
        for word in data:
            copy = word
            if is_word_in_base(copy, input_letters): 
                if len(word) == 6:
                    six_letter.append(word)
                elif len(word) == 5:
                    five_letter.append(word)
                elif len(word) == 4:
                    four_letter.append(word)
                elif len(word) == 3:
                    three_letter.append(word)
        #Printing the lists
        print("Six Letter words: \n", six_letter)
        print("Five Letter words: \n", five_letter)
        print("Four Letter words: \n", four_letter)
        print("Three Letter words: \n", three_letter)
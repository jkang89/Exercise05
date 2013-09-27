from sys import argv

script, inputfile = argv

print "We are now going to count how many of each letter we have."

our_file = open(inputfile).read()

list_of_characters = []
for char in our_file:
    char = str(char.lower())
    list_of_characters.append(char)
    #list_of_characters.sort()
#print list_of_characters

count = 0
char_var = 97

while char_var < 123:
    for i in list_of_characters:
        if ord(i) == char_var:
            count += 1
    print count
    count = 0
    char_var += 1
    

# for i in list_of_characters:
#     if ord(i) not in range(97,123):
#         list_of_characters.remove(i)
# print list_of_characters
    # char_var = 97
    # count = 0
    # for ord(char) in range(97, 123):
        
    #     if ord(char) == char_var:
    #         count += 1
    #         print char_var

    #     count(char_var)
    #     char_var += 1



    # for ord(char) > 96 and ord(char) < 123:
    #     print ord(char)


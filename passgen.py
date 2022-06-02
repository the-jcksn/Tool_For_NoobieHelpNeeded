list = input('Please enter the name of the wordlist to use (must be in the current directory: ')
password_list1 = []
password_list2 = []
final_list = []
special = ['!','£','$','%','^','#']
count = 0
input_list = []
with open(list, 'r') as words_in:
    for word in words_in:
        first_letter = word[:1]
        first_letter = first_letter.upper()
        minus_first = word[1:]
        capitalised = first_letter + minus_first
        input_list.append(capitalised)
for word in input_list:
    count += 1
    if count < len(input_list):
        word = word[:-1]
    for i in range(100):
        password = word + str(i)
        password_list1.append(password)
for password in password_list1:
        count2 = 0
        for word in input_list:
            count2 += 1
            if count2 < len(input_list):
                word = word[:-1]
            password2 = password + word
            password_list2.append(password2)
for character in special:
    for passwrd in password_list2:
        passwrd = passwrd + character
        final_list.append(passwrd)
        print(passwrd)
with open('output.txt','w') as output:
    for word in final_list:
        output.write(word)
        output.write('\n')
print('\nAll combinations saved to \'output.txt\'')

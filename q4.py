#Adam Belkacemi
#07/09/2025
#Ask the user to enter their favourite. If they enter 'red', 'RED', or 'Red' - display the message ' I like red too '. O therwise, display the message 'I dont like the colour <user_colour>, I prefer red'.
colour = input('Enter your favourite colour ')
if colour == 'Red' or colour == 'red' or colour == 'RED':
    print('I like red too')
else:
    print('I dont like',colour,"I prefer red")
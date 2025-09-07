#Adam Belkacemi
#07/09/2025
#Ask the user if it is raining. I ft hey enter 'yes or 'Yes' ask if it is windy. If they answer 'yes' or 'Yes' to the second question display the message 'It is too windy for an umbrella', otherwise, display the message 'Take an umbrella'. If they did not answer yes to the first question, display the answer 'Enjoy your day'
rain = input ("Is it raining ")
if rain == 'yes' or rain == 'Yes':
    wind = input ("Is it windy ")
    if wind == 'yes' or wind == 'Yes':
        print ('Its too windy to take an umbrella ')
    else:
        print ('Take an umbrella')
else:
    print("Enjoy your day")
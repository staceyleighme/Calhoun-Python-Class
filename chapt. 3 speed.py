#This is a program to show the user how much time will be saved (in minutes) if they drive at a speed higher than the posted speed limit

print('In this program you will choose your speed and distance')
print('If you want to go faster than the speed limit...')
print('This program will tell you how much time the faster speed saves you!')

limit=int(input('What is the posted legal speed limit in mph?'))
distance=int(input("What is the distance in miles?"))
average=int(input('Please enter the speed of your choice in mph.' ))


if average>limit:
    print("Let's see how much time you'll save by speeding!")

    time_legal=distance/limit

    print(f'The time to travel at the posted speed is {time_legal:,.9f}')

    time_inpspeed=distance/average
    print(f'The time to travel at the average speed of your choice is {time_inpspeed:,.9f}')

    subt_time=time_legal-time_inpspeed

    conv_min=subt_time*60
    print(f'Drving above the posted legal speed limit saved you {conv_min:,.0f} minutes!')


if average<=limit:print("You are a good citizen!")

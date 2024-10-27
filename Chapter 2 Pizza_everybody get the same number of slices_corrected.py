#In this program we are feeding a family of 4 pizza!
#There are 4 members of the family
#Everyone gets the same number of slices

slices_num=int(input('How many slices for per person? '))


family_total=slices_num*4




print(f'Then you will need {family_total} slices in total.')

print('One pizza has 8 slices.')

slices=8

whole_pizza=family_total/8

print(f'You will need to order {whole_pizza:,.0f} pizzas')

#calculate leftover slices

modus=family_total%8

leftover=slices-modus


print(f'You will have {leftover:.0f} leftover slices to enjoy tomorrow!')

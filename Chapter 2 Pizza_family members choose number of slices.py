#In this program 15 we are feeding a family of 4 pizza!

#Every family member gets to choose their number of slices

dad_num=int(input('How many slices for Dad? '))
mom_num=int(input('How many slices for Mom? '))
will_num=int(input('How many slices for Will? '))
shi_num=int(input('How many slices for Shiloh? '))

family_total=dad_num+mom_num+will_num+shi_num



print(f'Then you will need {family_total} slices in total.')

print('One pizza has 8 slices.')

slices=8

whole_pizza=family_total/8

print(f'You will need to order {whole_pizza:,.0f} pizzas')

#calculate leftover slices

modus=family_total%8

leftover=slices-modus


print(f'You will have {leftover:.0f} leftover slices to enjoy tomorrow!')








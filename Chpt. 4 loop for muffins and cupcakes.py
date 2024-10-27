#This program establishes a loop to sell muffins and cupcakes 
#until the inventory is depleted





muffins=10

keepgoing=True
while keepgoing:   
    
    MAX=10
    for counter in range(MAX):
        sale_muffin=int(input('How many muffins are you selling now? '))
        muffins=muffins-sale_muffin
        print(f'The number of muffins remaining in inventory is {muffins}')
        if muffins<1:
            break
            keepgoing=False


        print('out of stock')
        




cupcakes=10
keepgoing=True
while keepgoing:
    
    MAX=10
    for ounter in range (MAX):

        sale_cupcake=int(input('How many cupcakes are you selling now?'))
        cupcakes=cupcakes-sale_cupcake
        print(f'The number of cupcakes remaining in inventory is {cupcakes} ')
        if cupcakes<1:
            break
            keepgoing=False
        

        print('out of stock')
    

    


                
            

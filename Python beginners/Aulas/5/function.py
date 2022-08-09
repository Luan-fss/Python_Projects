# Def

def speed():
    # Code here when you call the function
    print ('urf urf')

speed() # Call the function

#####################################################################################

# Parameters mood / sobrenome
def luan (mood, sobrenome):
    if mood == 'Sad' and sobrenome == 'Santana':
        print(f"You're so Sad today {sobrenome}")
    else:
        print(f"You're very happy today {sobrenome}")

luan('Sad', 'Santana') # Answer the parameters

#####################################################################################

# Default parameters
def luan (mood = 'Happy'):
    if mood == 'Happy':
        print(f"You're so Happy")
    else:
        print(f"You're so Sad")

print('First time')
luan()
print('\nSecond time')
luan('Sad') 

####################################################################################

# Return Values (Use in functions)
def add_one(x):
    return x + 1
    
y = add_one(5)
print (y)


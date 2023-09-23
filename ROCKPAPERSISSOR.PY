import random

def userfunc():
    usernum = int(input("Enter rock-1, scissor-2, paper-3: "))
    if usernum == 1:
        userinput = 'rock'
    elif usernum == 2:
        userinput = 'scissor'
    elif usernum == 3:
        userinput = 'paper'
    else:
        print('Invalid input')
        return userfunc()

    return userinput


nooftimes = int(input('enter number of times you want to play prefer odd num'))
name = input("ENTER NAME:")
userscore = 0
computerscore = 0
while(nooftimes):
    user = userfunc()
    a = ['rock', 'paper', 'scissor']
    computer = random.choice(a)
    if(user == computer):
        userscore=userscore+1
        computerscore=computerscore+1        
    else:
        if(user == a[0]):
            if(computer == a[1]):
                computerscore = computerscore+1
            else:
                userscore =userscore+1
        if(user == a[1]):
            if(computer == a[2]):
                computerscore = computerscore+1
            else:
                userscore =userscore+1
        if(user == a[2]):
            if(computer == a[0]):
                computerscore = computerscore+1
            else:
                userscore =userscore+1
    nooftimes = nooftimes-1
 
if(userscore >= computerscore):
    print(name+" wins!")
else:
    print('computer wins!')

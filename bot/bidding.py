import time
from pytimedinput import timedInput
import pandas as pd
import random

Global_dict={'User':[], 'Bid_Amount':[] }


def get_other_user_details():
    pass #Extract the people details




def generate_bots():
    name=[]
    for i in range(0,9):
        k='bot'+str(i)
        name.append(k)
    return name




def bid_taken(names, price=10000):
    Global_dict['User'].append(names)
    Global_dict['Bid_Amount'].append(price)
    return

'''
class new_user:
    def __init__(self):
        self.name='x'#input('Enter name')
        self.other_details='x'#input('Enter other details')
    def pint(self):
        print('Name: ', self.name)
        print('Other_details: ', self.other_details)


class bidding(new_user):
    def __init__(self):
        self.type=1 #1 for practice and 0 for real time bidding
        if self.type==0:
            self.other_user = get_other_user_details()
        else:
            self.other_user = generate_bots()


x =  new_user()

x.pint()
'''
i=0
df=pd.DataFrame()
df['User']=['S']
df['Bid_amount']=['Y']
df.to_csv('Trail.csv')
#pd.DataFrame(columns=['User', 'Bid_amount']).to_csv('Trail.csv') #Here new table will be created in the database
bots = generate_bots()
user_name=input('Enter your name:  ')
names=[]
for f in bots:
    names.append(f)
names.append(user_name)
Move=False
bid_not_taken=names
while True:
    m=1
    if i>=10:
        break
    Move_to=i
    if i!=0:
        
        print('Current Bid is: ', i)
        print('Remaining Bids are as follows')
        for k in range(i, 10):
            print(k, ' Month bid')
        m, timedOut = timedInput("Move to which bid ", 10 )
        if timedOut:
            print('You didnt skip good going there are more stuff to learn')
            m=1
        else:
            m=int(m)-i
    for l in range(0, m):
        if len(bid_not_taken)==1:
            print('The bid is not available as the', bid_not_taken[0],'is remaining')
            nm = bid_not_taken[0]
            amt = 10000
            bid_taken(nm, amt)
            break
        c = random.randint(1,4)
        Bid_by_user=False
        amt=10000
        k=10000
        for o in range(0,c):
            if user_name not in bid_not_taken:
                time.sleep(5)
                random_name=random.choice(bid_not_taken[0:(len(bid_not_taken)-1)])
                nm=random_name
                amt = random.randint(7000, k)
                print(nm,'Has bid', amt)
                continue
            
            if Bid_by_user == False:
                tim = random.randint(0,10)
                k, timedOut = timedInput("Enter amount that has to be bid less than the previous bid: ", tim)
                if(timedOut):
                    k=amt
                    print('Someone else has taken the bid')
                    random_name=random.choice(bid_not_taken[0:(len(bid_not_taken)-1)])
                    nm = random_name
                    amt = random.randint(7000, k)
                    
                    print(nm,'Has bid', amt)
                else:
                    nm=user_name
                    amt = int(k)
                    print(nm, 'Has bid', amt)
                    Bid_by_user
            else:
                random_name=random.choice(bid_not_taken[0:(len(bid_not_taken)-1)])
                nm = random_name
                amt = random.randint(7000, k)
                print(nm,'Has bid', amt)
        print(bid_not_taken)
        print(nm,'HAS FINALIZED THIS AMOUNT: ', amt, ':):):);)')
        bid_taken(nm, amt)
        bid_not_taken.remove(nm)
        if nm==user_name:
            Bid_by_user=True

    i+=m


pd.DataFrame.from_dict(Global_dict).to_csv('Trail.csv')

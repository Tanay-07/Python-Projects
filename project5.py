master_password = input('what is the master password? ')
def view():
    with open('passwords.txt','r') as f:
       for line in f.readline():
           data=line.rstrip()
           user , passw = data.split('|')
           print('user:',user , '| password:',passw)

def add():
    name = input('Account name: ')
    pwd = input('password: ')
    with open('passwords.txt','a') as f:
        f.write(name + '|' + pwd + '\n')

while True:
    mode = input('would you like to add a new password or view existing ones(view/add),to quit type q')
    if mode == 'q':
        break
    if mode=='view':
        view()
    elif mode=='add':
        add()
    else:
        print('invalid')
        continue
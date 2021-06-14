from datetime import date
this_day = str(date.today())
extension = “.txt”
filename = this_day + extension 
f = open(filename,’w+’)
f = open(filename,”a”)
list = []
b = 1
while b==1:
        name = input(‘Enter your name :’)
        if name == ‘done’:
            f.close()
            exit()
        else:
            phone = input(‘Enter your phone no. :’)
            place = input(‘Enter your place :’)
            temp = input(‘Enter your temperature:’)
            list.append(name)
            list.append(phone)
            list.append(place)
            list.append(temp)
            f.write(str(list)+’\n’)
            list.clear()
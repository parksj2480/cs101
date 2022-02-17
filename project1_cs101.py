a=open("../project1/student_information.txt")

# 전역변수 
student_list   = []
attribute_name = None
attribute_type = None

### Start loading txt file and make variables ###
def Initiation():
    global attribute_name
    global attribute_type
    global student_list
    
    temp=a.readline()
    temp=temp.strip()
    temp=temp.split(", ")
    attribute_name=temp

    temp=a.readline()
    temp=temp.strip()
    temp=temp.split(", ")
    attribute_type=temp

    for line in a:
        temp=line.strip()
        temp=temp.split(', ')
        temp=tuple(temp)
        student_list.append(temp)
    return 


### Add student info into the student_list by tuple type.###
def Addition():
    print("write under formation \n ex: ",tuple(attribute_name))
    global student_list
    temp=input()
    student_list.append(temp)
    return

### Remove student information. ###
def Removal():
    global student_list
    number=-1
    
    condition=input("Input a condition -> ")
    if condition == 'all':
        student_list.clear()
        return
    condition=condition.split(' ')
    condition_name=condition[0]
    condition_bool=condition[1]
    condition_part=condition[2]
    temp=attribute_name.index(condition_name)
    
            
    for student in student_list:
        number += 1
        if temp == 0:
            if condition_part == student[temp]:
                print("Removed %s" % str(student_list.pop(number)))
    return

### Show some static analysis on the info ###
def Statistic():
    return

### Show information under certain conditions ###
def Show():
    cond = input("Input a condition -> ")
    if cond == 'all':
        for line in student_list:
            print(line)
        return
    cond=cond.split(' ')
    cond_name=cond[0]
    cond_bool=cond[1]
    cond_part=cond[2]
    number=-1
    temp=attribute_name.index(cond_name)

    for student in student_list:
        number += 1
        if cond_part == student[temp]:
            print(student)   
    return


### Correct existing information ###
def Write():
    return

### Start this program it may loop letting you to choose particular activation ###
def main():
    return

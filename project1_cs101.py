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
def Addition(info):
    print("write under formation \n ex: ",tuple(attribute_name))
    global student_list
    student_list.append(info)
    return

### Remove student information. ###
def Removal():
    global student_list
    condition=input()
    for student in student_list:
        student.remove(info)
    return

### Show some static analysis on the info ###
def Statistic():
    return

### Show information under certain conditions ###
def Show():
    return


### Correct existing information ###
def Write():
    return

### Start this program it may loop letting you to choose particular activation ###
def main():
    return

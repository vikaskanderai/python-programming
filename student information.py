print("Enter student information in the order NAME AGE CONTACT-NUMBER EMAIL-ID")

import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell()== 0:
             writer.writerow(["Name","Age","Contact-number","Email-ID"])


        writer.writerow(info_list)



condition=True
num=1
while(condition):
    student_info=input("Enter the information of student number {}:".format(num) )
   
    student_info_list= student_info.split(" ")
    print("The entered information is \nName: {} \nAge: {}\nContact-number: {}\nEmail-ID: {}".format(student_info_list[0],
                                                                                                     student_info_list[1],student_info_list[2],student_info_list[3]))
    info_check= input("Enter (yes) if the information entered is correct else enter (no): ")

    if info_check == "yes" :
        write_into_csv(student_info_list)

        condition_check= input("Enter (yes/no) if u want to enter the information of another student: ")
        if condition_check == "yes":
            condition=True
            num=num+1
        elif condition_check== "no":
            condition=False  


    elif info_check =="no":
        print("\n!!! Pelase enter the information again !!!")
        

          
    
    

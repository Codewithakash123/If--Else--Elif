marks = int(input("Enter your marks:"))
if(marks < 0 or marks > 100):
    print("Invalid marks")
else:
    if(marks>=91 and marks<=100):
        Grade = "O"
        Message = "Phenomenal"
    elif(marks>=81 and marks<=90):
        Grade = "A+"
        Message = "Excellent"
    elif(marks>=71 and marks<=80):
        Grade = "A"
        Message = "keep it up"
    elif(marks>=61 and marks<=70):
        Grade = "B+"
        Message = "very good"
    elif(marks>=61 and marks<=70):
        Grade = "B"
        Message = "good"
    elif(marks>=51 and marks<=60):
        Grade = "C"
        Message = "Push Forward"
    else :
        Grade = "U"
        Message = "You must work hard"
print("Marks:",marks)
print("Grade:",Grade)
print("Message:",Message)


    

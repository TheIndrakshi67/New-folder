Eng= int(input(" Enter your marks for english "))
Math= int(input(" Enter your marks for maths "))
Science= int(input(" Enter your marks for science  "))
Social= int(input(" Enter your marks for Social studies "))
lang= int(input(" Enter your marks for language "))

avg= (Eng+Math+Science+Social+lang)//5

if avg>90:
    print("Grade: A")
elif avg>70:
    print("Grade B")
elif avg>50:
    print("Grade C")
else:
    print("YOu failed)")
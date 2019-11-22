m1=int(input("enter m1 marks:"))
m2=int(input("enter m2 marks:"))
m3=int(input("enter m3 marks:"))
sum=0
per=0

diff=0
if(m1>=40 and m2>=40 and m3>=40):
    sum = m1 + m2 + m3
    print("total marks=", sum)
    per = sum / 3
    print("perscentage:", per)
    print("pass")
elif(m1<=40 or m2<=40 or m3<=40):
    count=0
    if m1<40:
        count+=1
    if m2<40:
        count+=1
    if m3<40:
         count+=1

    if count==1:
        if m1<40:
            diff=40-m1
            if diff > 8:
                print("fail")
            else:
                m1+=diff
                print("pass with grace",diff,"marks in m1")
        elif m2<40:
            diff = 40 - m2
            if diff > 8:
                print("fail")
            else:
                m2 += diff
                print("pass with ",diff)
        elif m3<40:
            diff = 40 - m3
            if diff > 8:
                print("fail")
            else:
                m3 += diff
                print("pass with",diff)
    elif count>1:
        print("FAIL")

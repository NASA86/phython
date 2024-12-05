class multiplefunctions():
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
    def OddEven():
        num=(int(input("Enter a number:")))
        if((num%2)==0):
            print(num,"is Even number")
        else:
            print(num,"is odd number")
    def Elegible():
        gender=input("Your gender:")
        age=int(input("Your age:"))
        if((gender=="Male") and (age>=21)):
             print("ELIGBLE")
        elif((gender=="Female") and (age>18)):
              print("ELIGBLE")
        else:
            print("NOT ELIGBLE")
    def percentage():
        subject1=int(input("Subject1="))
        subject2=int(input("Subject2="))
        subject3=int(input("Subject3="))
        subject4=int(input("Subject4="))
        subject5=int(input("Subject5="))
        total=subject1+subject2+subject3+subject4+subject5
        print("Total:",total)
        precentage=float((total/500))*100
        print("Precentage:",precentage)
    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth"))
        print("Area formula: (Height*Breadth)/2")
        triangle=(height*breadth)/2
        print("Area of Triangle:",triangle)
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth1=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        formula=height1+height2+breadth1
        print("Perimeter formula:",formula)
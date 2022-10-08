#-------------------------------------------------------------------------------
# Name:       Golden Project 2
# Purpose:
#
# Author:      rounakverma421@gmail.com
#
# Created:     08-10-2022
# Copyright:   (c) hp 2022

#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()




#Golden Project  2
#Mini Perimeter and area Calculator#
#Project Made By Rounak Verma


name = input("Hi Welcome here on this mini calculator , Enter  Your Name here");
ok = input("We are glad to have you here "+ " " + name + " " + "Type Ok To proceed Further");
note = input("Note-This calculater Can Only calculate Values in cm square and meter sqaures.Type Ok To move!");

print("Which figure Would you like to work with today?? ");
print ("Enter the alloted shape numeric value.");
print ("Square = 1");
print ("Right Angled Triangle = 2");
print ("Rectangle = 3");




#taking the input from the user on which figure he will like to work upon#

figure = input("Enter The number Of the figure You will like to work upon today : ");
figure = int(figure);




#giving the further Conditions as soon as the user enters teh numeric values#
if figure == 1 :


   #Taking the operation from the user #
   operation1= input("For Area Press  1 and for perimeter Press 2.")
   operation1= int(operation1);

   if operation1 == 1  :


       sideSquare=input("Enter the Length Of any side of your Choice")
       #converting the user's input into a numeric value#
       sideSquare= int(sideSquare)


       squareArea =(sideSquare*sideSquare);
       #Now again converting This final area of the sqaure into the string
       squareArea= str(squareArea);


       #Giving A statement for displaying the units in the final Results#

       #Asking For the units of the length In the figure#
       unit = input("Your Length is in centimeter then press 1 and if it is in Meters press 2");
       unit = int(unit);

       if unit == 1 :
          displayUnit = ("centimeter Sqaure")
       else :
          displayUnit = ("Meter Square")


       display = input("So hence the area Of this figure  Is : "+ " "+ squareArea +" "+ displayUnit);

   elif operation1 == 2:

        lengthSqaure = input("Enter The length of Any side :");
        lengthSquare = int(legthSquare);

        #giving the statement for the perimeter of the square#
        perimeterSqaure = (4 * lengthSqaure);

        #Converting the value os the perimeter of the square into the string#
        perimeterSquare = str(perimeterSqaure);

         #Giving A statement for displaying the units in the final Results#

       #Asking For the units of the length In the figure#
        unit = input("IF Your Length is in centimeter then press 1 and if it is in Meters press 2");
        unit = int(unit)
        if unit == 1 :
          displayUnit = ("centimeter Sqaure")
        elif unit == 2 :
          displayUnit = ("Meter Square");
        else :
          print("Invalid Input");


        Display5 = input("Hence the perimeter of the square is "+" "+ perimeterSqaure +" "+ displayUnit);

   else :
    print("Invalid Statement");


elif figure == 2:


    #Taking the operation from the user #
    operation2= input("For Area Press  1 and for perimeter Press 2.")

    operation2 = int(operation2);

    if operation2 == 1:


       perpendicular = input("Enter the length of perpendicular of the triangle");
       perpendicular = int(perpendicular);


       base = input("Enter the length of the base ");
       base = int(base);

       area = ((base * perpendicular)*1/2);
       area = str(area);

       #Giving A statement for displaying the units in the final Results#

       #Asking For the units of the length In the figure#
       unit = input("If Your Length is in centimeter then press 1 and if it is in Meters press 2");
       unit = int(unit);

       if unit == 1 :
          displayUnit = ("centimeter Sqaure");
       elif unit == 2 :
          displayUnit = ("Meter Square");
       else :
          print("Invalid Syntax");


       print("Hence the final area of your right angled triangle is "+ area+" "+ displayUnit);


     #giving the statement for the perimeter of the triangle#
    elif operation2 ==2:

        side1 = input("Enter The Length Of Side1");
        side1=int(side1);

        side2 = input("Enter The Length Of Side2");
        side2=int(side2);

        side3 = input("Enter The Length Of Side3");
        side3=int(side3);

        perimeterTriangle = (side1+side2+side3);
        perimeterTriangle = str(perimeterTriangle);

         #Giving A statement for displaying the units in the final Results#

       #Asking For the units of the length In the figure#
        unit = input("Your Length is in centimeter then press 1 and if it is in Meters press 2");
        unit = int(unit)
        if unit == 1 :
          displayUnit = ("centimeter Sqaure");
        elif unit == 2 :
          displayUnit = ("Meter Square");
        else :
            print("Invalid Syntax");

        #Giving A display statement for the screen#
        display7 = Input("Hence, your final perimeter for your triangle is" +" "+ perimeterTriangle+ " " + displayUnit);

    else :
        print("Invalid Syntax");

#giving the commands for the rectangular figures#
elif figure == 3 :



    #Taking the operation from the user #

    operation3= input("For Area Press  1 and for perimeter Press 2.")
    operation3 = int(operation3);


    if operation3 == 1 :
       lengthRectangle = input("Enter The length of The desired rectangle");
       lengthRectangle = int(lengthRectangle);


       breadthRectangle = input("Enter The breadth of the rectangle");
       breadthRectangle = int(breadthRectangle);


       rectangleArea = (lengthRectangle * breadthRectangle);
       rectangleArea = str(rectangleArea);

       #Giving A statement for displaying the units in the final Results#

       #Asking For the units of the length In the figure#
       unit = input("Your Length is in centimeter then press 1 and if it is in Meters press 2");
       unit = int(unit);


       if unit == 1 :
          displayUnit = ("centimeter Sqaure");
       elif unit == 2 :
          displayUnit = ("Meter Square");
       else :
        print("Invalid Syntx");

       display8 = input("Hence the final Area is "+rectangleArea +" " + displayUnit);

    elif operation3 == 2 :

       lengthRectangle = input("Enter The length of The desired rectangle");
       lengthRectangle = int(lengthRectangle);


       breadthRectangle = input("Enter The breadth of the rectangle");
       breadthRectangle = int(breadthRectangle);

       perimeterRectangle = 2*(lengthRectangle+lengthRectangle);
       perimeterRectangle = str(perimeterRectangle);

        #Giving A statement for displaying the units in the final Results#

       #Asking For the units of the length In the figure#
       unit = input("Your Length is in centimeter then press 1 and if it is in Meters press 2");
       unit = int(unit);


       if unit == 1 :
          displayUnit = ("centimeter Sqaure");

       elif unit == 2 :
          displayUnit = ("Meter Square");

       else :
          print ("Invalid Syntax")



       finalStatement = input("Hence, your final perimeter is"+ " "+ perimeterRectangle +" " + displayUnit);


    else :
        print("Invalid Syntax");



display1 = input("Thankyou For Using This Calculator .I Hope you loved it .Click Ok");
display2 = input("For Any Queries or feedbacks please feel free to reach us. click Ok");
display3 = input("rounakverma421@gmail.com .....Click Ok To exit");






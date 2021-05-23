# in this function we can solve Questions 1 , 2 , 3 , 4 , 5 and 6 from the work sheet

def physics_cal():
    #because the user will choose from the list we have to use While true
    while True:
        print("------------------------------------")
        print("a. The Equation for Time")
        print("b. The Equation for Acceleration")
        print("c. The Equation for Speed")
        print("d. The Equation for Distance")
        print("e. for closing the program")
        print("------------------------------------")
        # response is the user choose from the list
        response = input(" choose a letter from a-e : ")

        # this block is for the  time equation and the user will enter the distance and speed
        if response.lower() == "a":

            distance = float(input(" Enter the distance:"))
            speed = float(input(" Enter the speed:"))
        # the result
            print("The time is",( distance/ speed ),"s")

        #this block is for the acceleration equation
        elif response.lower() == "b":
            vf = float(input(" Enter the VF:"))
            vi = float(input(" Enter the VI:"))
            time = float(input(" Enter the Time in s :"))
            # the result
            print("The Accleration is", ((vf - vi) / (time / 3600)), "m/s^2")

        # this block is for the speed equation
        elif response.lower() == "c":

            distance = float(input(" Enter the Distance:"))
            time = float(input(" Enter the Time:"))
            # the result
            print("The speed is", ( distance / time),"m/s")

        # this block is for the Distance equation
        elif response.lower() == "d" :
            # the user will enter the numbers here
            speed = float(input(" Enter the speed :"))
            speed_unit = input(" Enter the unit of speed : km/hr or m/s:")
            time = float(input(" Enter the time:"))

            # here the user can enter the number and Determine the unit if its ( km/hr ) or ( m/s)
            if speed_unit.lower() == "km/hr":
                print("The Distance is ", ( speed * time), "km")

            elif speed_unit.lower() == "m/s" :
                time_unit = input(" Enter the unit of Time : s or m ")

                # if the user has chosen m/s , now he have to choose the unit of the time ( seconds ) or ( minutes )
                if time_unit.lower() == "m":
                    print("The Distance is :",( speed * (time * 60)), "m")   # when the user chose minutes
                else :
                    print("The Distance is ", (speed * time), "m")   # when the user chose seconds

        # finally this block is for exiting the program
        elif response.lower() == "e":
            print(" closing the program...")
            print(" Thank you")
            break


# initiate the universal function
print(physics_cal())








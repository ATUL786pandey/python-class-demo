total=0
while True:
    print("**********WELCOME TO RADHA KRISHNA HOTEL*************")
    print("v for veg")
    print("n for nonveg")
    print("e for exit")
    ch=input("enter your choice => ")
    print("*************************************************")
    if ch=='v':
        while True:
            print("s for starter")
            print("m for maincourse")
            print("d for desert")
            print("e for exist")
            ch1=input("enter your choice =>")
            print("****************************************")
           
            if ch1=='s':
                while True:
                    
                    print("p for paneer tikka \t 150\na for aaloo tikki \t 120\nc for cheese ball \t 180\ne for exit")
                    ch2=input("enter the choice => ")
                    if ch2=='p':
                        
                        p=int(input("enter the quantity=> "))
                        total=total+(p*150)
                    elif ch2=='a':
                        
                        a=int(input("enter the  quantity => "))
                        total=total+(a*120)
                    elif ch2=='c':
                        
                        c=int(input("enter the  quantity => "))
                        total=total+(c*180)
                        #print("total is {}".format(total))
                    elif ch2=='e':
                         break
                    else:
                        print("invalid input ")

                        
                   
                   
            elif ch1=='m':
                while True:
                    
                    print("pk for paneer kholapuri \t 175\npt for paneer Tikka masala \t 190\nv for veg kholapuri \t\t 160\ne for exit")
                    ch2=input("enter your choice => ")
                    if ch2=='pk':
                        pk=int(input("enter the quantity => "))
                        total=total+(pk*175)
                    elif ch2=='pt':
                        pt=int(input("enter the qty => "))
                        total=total+(pt*190)
                    elif ch2=='v':
                        v=int(input("enter the qty =>  "))
                        total=total+(v*160)
                    elif ch2=='e':
                        break
                    else:
                    
                        print("invalid input")
                        
                   
            elif ch1=='d':
                while True:
                    
                    print("v for vanila icecream \t\t 80 \np for pista icecream \t\t 90 \nc for chocobar icecreame \t 55\ne for exit")
                    ch3=input("enter the choice => ")
                    if ch3=='v':
                        v=int(input("enter the qty =>"))
                        total=total+(v*80)
                    elif ch3=='p':
                        p=int(input ("enter the qty =>"))
                        total=total+(p*90)
                    elif ch3=='c':
                        c=int(input("enter the qty =>"))
                        total=total+(c*55)
                    elif ch3=='e':
                        break
                    else:
                        print("invalid input")
                        
                
            elif ch1=='e':
                break
            else:
                print("invalid input")
            
                
                
           
        
    elif ch=='n':
        while True:
            print("s for starter")
            print("m for maincourse")
            print("d for desert")
            print("e for exist")
            ch1=input("enter your choice =>")
            print("****************************************")
           
            if ch1=='s':
                while True:
                    
                    print("cp for chiken  pakora \t\t 195\nhc for hariyali chicken kabab \t 220\ncr for chicken rosted \t\t 195\ne for exit")
                    ch2=input("enter the choice => ")
                    if ch2=='cp':
                        cp=int(input("enter the quantity=> "))
                        total=total + (cp*195)
                    elif ch2=='hc':
                        hc=int(input("enter the  quantity => "))
                        total=total + (hc*220)
                    elif ch2=='cr':
                        cr=int(input("enter the  quantity => "))
                        total=total+(cr*195)
                        #print("total is {}".format(total))
                    elif ch2=='e':
                        break
                    else:
                    
                        print("invalid input ")
                        
                    
                        
            elif ch1=='m':
                while True:
                    
                    print("cl for chicken masala \t\t\t 210\ncc for chicken curry \t\t\t 170\ncj for chicken jalfrezi \t\t 250\ne for exit")
                    ch2=input("enter your choice => ")
                    if ch2=='cl':
                        cl=int(input("enter the quantity => "))
                        total=total+(cl*210)
                    elif ch2=='cc':
                        cc=int(input("enter the qty => "))
                        total=total+ (cc*170)
                    elif ch2=='cj':
                        cj=int(input("enter the qty =>  "))
                        total=total+(v*250)
                    elif ch2=='e':
                        break
                    else:
                        print("invalid input")
                    
            elif ch1=='d':
                while True:
                    
                    print("v for vanila icecream \t\t 80 \np for pista icecream \t\t 90 \nc for chocobar icecreame \t 55\ne for exit")
                    ch3=input("enter the choice => ")
                    if ch3=='v':
                        v=int(input("enter the qty =>"))
                        total=total+(v*80)
                    elif ch3=='p':
                        p=int(input ("enter the qty =>"))
                        total=total+(p*90)
                    elif ch3=='c':
                        c=int(input("enter the qty =>"))
                        total=total+(c*55)
                    elif ch3=='e':
                        break
                    else:
                        print("invalid input")
            
            elif ch1=='e':
                break
            else:
                print("invalid input")
                   
    
                
            
         
    
             
    elif ch=='e':
        break
    else:
        print("invalid input")

total1=total*0.18
print("Thank u visit again........")
print("your total bill is {}".format(total1))

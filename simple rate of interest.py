

#*** WAP TO FIND SIMPLE INTEREST OF USER ENTER AMOUNT YEAR RATE***

amt=float(input("Enter the amount   " ))
year=float(input("Enter the no of year  "))
roi=float(input("Enter the rate of interest  "))
smi=amt*year*roi/100
print ( "simple rate of interest of amount {} year {} roi {} is smi {}".format(amt,year,roi,smi))

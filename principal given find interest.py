
#*** WAP TO CALCULATE THE INTEREST ON PRINCICAL,YEAR,AND RATE OF INTEREST***

amt=float(input("enter the amount => "))
year=float(input("enter the no of year => "))
roi=float(input("enter the rate of interest => "))
smi=amt*year*roi/100
print ("interest on amount = {},year = {},roi = {} is = {}".format(amt,year,roi,smi))

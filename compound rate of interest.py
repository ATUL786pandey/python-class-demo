#*** WAP TO FIND THE COMPOUND INTEREST and simple interset***


amt=float(input("Enter the amount ==>"))
roi=float(input("Enter the rate of interest ==>"))
year=float(input("Enter the no year ==> "))
smi=amt*roi*year/100
print("interest for the amount {},rate {} , year {} is smi {}".format(amt,roi,year,smi))
comi=amt*(1+roi/year)**year
print ("compound rate of interest of amount {},rate {} and year {} is comi {}".format(amt,roi,year,comi-amt) )

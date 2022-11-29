import FormatValues as FV
import datetime
Today = datetime.datetime.now()

'''
# Open the defaults file and read the values into variables
f = open('Def.dat', 'r')
ClaimNum = int(f.readline())
HSTRate = float(f.readline())
f.close()

print(ClaimNum)
print(HSTRate)

# Initialize any counters or accumulators
InvCtr = 0
InvReorderCtr = 0
ZeroCtr = 0
ItemsOnOrderCtr = 0

TotInvCostAcc = 0
TotInvRetailAcc = 0

WinterCtr = 0
SpringCtr = 0
SummerCtr = 0
FallCtr = 0

f = open("SummaryInv.dat", "r")
for InventoryData in f:
       InvLine = InventoryData.split(",")
       ProdCost = float(InvLine[3].strip())
       RetailPrice = float(InvLine[4].strip())
       QOH = int(InvLine[5].strip())
       ReorderPt = int(InvLine[6].strip())
       Winter = InvLine[8].strip()
       Spring = InvLine[9].strip()
       Summer = InvLine[10].strip()
       Fall = InvLine[11].strip()
       ActDelDate = InvLine[16].strip()
       ActDelDate = datetime.datetime.strptime(ActDelDate, "%Y-%m-%d")


       InvCtr += 1

       if QOH < ReorderPt:
              InvReorderCtr += 1

       if QOH == 0:
              ZeroCtr += 1

       if ActDelDate > Today:
              ItemsOnOrderCtr += 1

       TotInvCostAcc += ProdCost * QOH
       TotInvRetailAcc += RetailPrice * QOH
       PotProfMargin = TotInvRetailAcc - TotInvCostAcc

       if Winter == "Y":
              WinterCtr += 1
       if Spring == "Y":
              SpringCtr += 1
       if Summer == "Y":
              SummerCtr += 1
       if Fall == "Y":
              FallCtr += 1

       ClaimNum += 1

f.close()

# Now print out the results
print(f"Total inventory items:     {InvCtr:>4d}     Total inventory cost:     {FV.FDollar2(TotInvCostAcc):>10s}")
print(f"Items to order:             {InvReorderCtr:>3d}     Total inventory retail:   {FV.FDollar2(TotInvRetailAcc):>10s}")
print(f"Items with 0 on hand:       {ZeroCtr:>3d}     Potential profit margin:  {FV.FDollar2(PotProfMargin):>10s}")
print(f"Items currently on order:   {ItemsOnOrderCtr:>3d}")
print()
print(f"Winter {WinterCtr:>3d}      Spring: {SpringCtr:>3d}       Summer: {SummerCtr: >3d}       Fall: {FallCtr:>3d}")

f = open('Def.dat', 'w')
f.write("{}\n".format(str(ClaimNum)))
f.write("{}\n".format(str(HSTRate)))
f.close()
'''

FirstName = input("Enter the first name: ").title()
LastName = input("Enter the last name: ").title()
print("  First name: {:<8} Last name: {:<8}".format(FirstName, LastName))
print(f"  First name: {FirstName:<8} Last name: {LastName:<8}")

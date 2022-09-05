itemp= {"Iphone 10":120000, "PSP4":57600, "Splendor Top G1_series":123000,"Supercomputer T1_series":260000}
oritem=[]
item={1:"Iphone 10",2:"PSP4",3:"Splendor Top G1_series",4:"Supercomputer T1_series"}
i=0
print("List of Items Available in Megastore")
print('1.Iphone 10-Rs.120000\n2.PSP4-Rs.57600\n3.Splendor Top G1_series-Rs.123000\n4.Supercomputer T1_series-Rs.260000\n5.n6.Exit')
print("Enter your choice from 1 to 5 for purchase & 6 for Exit")
t=int(input())
while((t>=1)and (t>=5)):
   i= i+1
   print('Number of quantity required')
   n=int(input())
   t1=item[t]
   t2=item[t1]
   tc=n*t2
   oritem=oritem+[item[t], item[t1],n,tc]
   print("List of Items Available in Megastore")
   print('1.Iphone 10-Rs.120000\n2.PSP4-Rs.57600\n3.Splendor Top G1_series-Rs.123000\n4.Supercomputer T1_series-Rs.260000\n5.n6.Exit')
   print("Enter your choice from 1 to 5 for purchase & 6 for Exit")
   t=int(input())
print("Retail Bill System")
print("***********************************************************")   
print('Name \t Price \t Qunatity \t Total')
print("-----------Always Welcomes You, Have a Nice Day------------")
ct=0
ind=0
for x in range(i):
    print("%s\t%0.2f\t\t%d\t\t%0.2f"  %(oritem[ind],oritem[ind+1],oritem[ind+2],oritem[ind+3]))
    ct=ct+oritem[ind+3]
    ind4=ind+4
    print("---------------------------Thanks-----------------------")
    print("Total Amount %0.2f"%ct)
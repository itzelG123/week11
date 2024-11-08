#nested loops = a loop within another loop(outer,inner)
            #outer loop  
                #inner loop

# for x in range(1,10):#1 is inclusive and 10 is exclusive
#     print(x)
#     print(x,end=' ')

# for x in range(3):
#     for x in range(1,10):
#         print(x,end='/n')

rows =int(input("enter num of rows:"))
columns=int(input("enter num of colums"))
symbol=int(input("enter symbol to use"))

for x in range(rows):
     for y in range(columns):
        print(symbol,end='')
     print()
# Task 01
ITEM_Codes=["A1","A2","B1","B2","B3","C1","C2","C3","D1","D2","E1","E2","E3","F1","F2","G1","G2"]
ITEM_Description=["Comapct Case","Tower Case","8GB RAM","16GB RAM","32GB RAM","1 TB HDD (Main)","2 TB HDD (Main)","4 TB HDD (Main)","240 GB SSD (Solid state)","480 GB SSD (Solid state)","1 TB HDD (Second)","2 TB HDD (Second)","4 TB HDD (Second)","DVD/Blu-Ray player (Optical)","DVD/Blu-Ray Re-writer","Standard Version (operating system)","Professional Version (Operating system)"]
ITEM_Price=[75.00,150.00,79.99,149.99,299.99,49.00,89.99,129.99,59.99,119.99,49.99,89.99,129.99,50.00,100.00,100.00,175.00]

print("Welcom to the online computer Shop!")

case_code=input("please Choose a case (A1 or A2): ")
ram_Code=input("please Choose a ram modile (B1 or B2 or B3)")
hdd_code=input("please Choose a main disk drive (C1 or C2 or C3)")

if case_code not in ITEM_Codes or ram_Code not in ITEM_Codes or hdd_code not in ITEM_Codes:
    print("Invalid input. Please try again")
    exit()

computer_price=ITEM_Price[ITEM_Codes.index(case_code)]+ITEM_Price[ITEM_Codes.index(ram_Code)]+ITEM_Price[ITEM_Codes.index(hdd_code)]

print("you have chosen the following item:")
print("-Case:",ITEM_Description[ITEM_Codes.index(case_code)])
print("-Ram :" ,ITEM_Description[ITEM_Codes.index(ram_Code)])
print("-main hard disk drive :",ITEM_Description[ITEM_Codes.index(hdd_code)])
print("The total price of the computer is :",computer_price)


# Task 02
print("do you want to purchase any item? (Y/N)")
answer=input()
if answer.upper()=="Y":
    additional_items=[]
    for i in range(len(ITEM_Codes)):
        if ITEM_Codes[i] not in [case_code,ram_Code,hdd_code]:
            print(ITEM_Codes[i],ITEM_Description[i],ITEM_Price[i])
            additional_items.append(ITEM_Codes[i])

    selected_additonal_items=[]
    for i in range(len(additional_items)):
        print(f"please enter the numbberof {additional_items[i]} s you want to purchase (0 or 1): ")
        quantity=int(input())
        if quantity == 1:
            selected_additonal_items.append(additional_items[i])
else:
   selected_additonal_items = []

for item in selected_additonal_items:
    computer_price += ITEM_Price[ITEM_Codes.index(item)]
print("you have chosen the following additional item:")
for item in selected_additonal_items:
    print(item,ITEM_Description[ITEM_Codes.index(item)])
print("the new price of the computer is : ",computer_price)


# Task 03
num_additional_item=len(selected_additonal_items)
if num_additional_item>0:
    discount_rate=0.05 if num_additional_item==1 else 0.10
    discount_amount=computer_price * discount_rate
    computer_price -= discount_amount
    print("you have saved",discount_amount,"thanks to our discount!")
    print("the new price of the computer is:", computer_price)
else:
    print("you have not bought any additional item, so you are not eligible for a discount. ")


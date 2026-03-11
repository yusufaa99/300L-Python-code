print("Welcome to Book Shipping App\n")

price = 24.95
discount = ((price*0.4))
shipping1 = 3
shipping2 = (0.75)

print("Enter Number Of Copies :")
copies = int(input())

first_copy_price = ((price-discount)+shipping1)
remaining_copy_price = ((price-discount)+shipping2)
total_cost = ((first_copy_price)+(remaining_copy_price*(copies-1)))

print("The total cost of shipping".title(), copies, "books is :".title() ,round(total_cost, 2))


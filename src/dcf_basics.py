
def get_user_cash_flows():   
    year = []    
    num_years = int(input("How many years of cash flows? "))  
    for i in range(num_years):
            year_cf = int(input(f"Enter cash flow for year {i+1}: "))             
            year.append(year_cf)
    return  year
        

def calculate_total_pv(cash_flows, discount_rate):                         # defined function and its parameters  
    present_values = []                                                    # empty  list that will store the present values

    for i , item in enumerate(cash_flows,start=1):                         # loop that will repeat, i is the counter that starts from 1
        pv = item / (1 + discount_rate)**i
        print("Year:",i, "- Cash FLow:", item)
        print("Year:",i,"- Present Value:", pv)   
        present_values.append(pv)                                       # storing present values 
    total_pv = sum(present_values)                                          
    return total_pv                                                         # returing value of total present value outside the function                            # Printing  Total Present Value

user_cash_flows = get_user_cash_flows()
rate = float(input("Enter discount rate (e.g. 0.10): "))
final_result = calculate_total_pv(user_cash_flows, rate)
print("Your Total Present Value is:", final_result)
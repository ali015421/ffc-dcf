cash_flow = [200, 250, 300]
discount_rate = 0.10

def calculate_total_pv(cash_flows, discount_rate):                         # defined function and its parameters  
    present_values = []                                                    # empty  list that will store the present values

    for i , item in enumerate(cash_flows,start=1):                         # loop that will repeat, i is the counter that starts from 1
            pv = item / (1 + discount_rate)**i
            print("Year:",i, "- Cash FLow:", item)
            print("Year:",i,"- Present Value:", pv)   
            present_values.append(pv)                                       # storing present values 
    total_pv = sum(present_values)                                          
    return total_pv                                                         # returing value of total present value outside the function

result = calculate_total_pv(cash_flow, discount_rate)                       # calculating total present value        
print("The Total Present Value is:",result)                                 # Printing  Total Present Value

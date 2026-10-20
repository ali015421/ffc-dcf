cash_flows = [200, 250, 300]
discount_rate = 0.10

def calculate_total_pv(cash_flows, discount_rate):
    present_values = []
    for i , item in enumerate(cash_flows,start=1):
            pv = item / (1 + discount_rate)**i
            print("Year:",i, "- Cash FLow:", item)
            print("Year:",i,"- Present Value:", pv)   
            present_values.append(pv)
    total_pv = sum(present_values)
    return total_pv
result = calculate_total_pv(cash_flows, discount_rate)
print("The Total Present Value is:",result)

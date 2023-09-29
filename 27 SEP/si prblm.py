total_amount=int(input())
i=int(input())
m5=int(input())
m9=int(input())
intrest_upto_5months=(total_amount*4/12*i)/100;
intrest_upto_9months=((total_amount-m5)*4/12*i)/100;
remaining_months=((total_amount-m5+m9)*4/12*i)/100;
print((total_amount-m5+m9)+intrest_upto_5months+intrest_upto_9months+remaining_months)
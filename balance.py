balance = 1000
interest = 1.05

print(f'your balance after 5 years is {balance * interest * interest * interest * interest * interest}')
balance *= interest
print(f'your balance y1  is {balance}')
balance *= interest
print(f'your balance y2 is {balance}')

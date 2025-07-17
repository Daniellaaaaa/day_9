# Python class task
allowance = 2000
print(f"My Allowance is: N{allowance}")

# 1. spent N400
allowance -= 400
print(f"I spent N400 on books so my balance is: N{allowance}")

# 2. add N100
allowance += 100
print(f"Found N100 under the bed so my balance is: N{allowance}")

# 3. bought snacks N250
allowance -= 250
print(f"Bought snacks for N250 so my balance is: N{allowance}")

# 4. gave 25% of my balance
remove = (allowance * 25) / 100
#allowance -= (allowance * 0.25)
allowance -= remove
print(f"Gave 25 percent of my balance to my sigbling so my current balance is {allowance}")

# 5. I used one-third of my balance
remove2=allowance / 3
allowance -= remove2
print(f"I used one-third of my balance so current balance is: N{allowance}")

# 6. split the remaining balance
allowance //= 2
print(f"I split my balance into 2 so my current balance is: N{allowance}")

# 7. using modulus to calculate the remainder
allowance %= 100
print(f"The remainder is: {allowance}")

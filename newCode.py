def pow(base, exp):
    if exp ==0:
        return 1
    else:
        return base * pow(base,exp-1)

print(pow(2,5))

itemPrice = int(input("물건값을 입력하시오:"))
note = int(input("1000원 지폐 개수:"))
coin500 = int(input("500원 동전 개수:"))
coin100 = int(input("100원 동전 개수:"))
change = note*1000 + coin500*500 + coin100*100 - itemPrice
nCoin500 = change//500
nCoin100 = change//100
change = change%100
change = change%500
nCoin10 = change//10
change = change%10
nCoin1 = change
print("500원=", nCoin500, "100원=", nCoin100, "10원", "1원=", nCoin1)
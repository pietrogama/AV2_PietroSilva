
account_balance = 900
response = "yes"  


processamento = (
    (lambda withdrawal, balance:
        ("Withdrawal not allowed", balance)) 
    if response == "no"
    else (lambda withdrawal, balance:
        ("Withdraw amount then update account balance", balance - withdrawal)))(300, account_balance)


result, account_balance = processamento


deposit_amount = 200
account_balance += deposit_amount


print(f"Resultado do Saque: {result}")
print(f"Saldo da conta após o deposito: {account_balance}")

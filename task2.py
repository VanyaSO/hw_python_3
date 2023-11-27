# Користувач вводить із клавіатури три числа. 
# Перше число — зарплата за місяць, 
# друге число — сума місячного платежу за кредитом у банку, 
# третє число ­— заборгованість за комунальні послуги. 
# Необхідно вивести на екран суму, яка залишиться у користувача після всіх виплат.

month_salary = float(input("Enter monthly salary: "));
month_payment_bank = float(input("Enter monthly payment for a loan from a bank: "));
deb_utility = float(input("Enter debt for utility services: "));

balance_post_pay = month_salary - month_payment_bank - deb_utility;

print(f"Your balance after all payments {balance_post_pay}");

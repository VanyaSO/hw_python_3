# Напишіть програму, що обчислює площу ромба.
# Користувач вводить із клавіатури довжину двох його діагоналей.

diagonal_first = float(input("Enter first diagonal: "));
diagonal_fecond = float(input("Enter second diagonal: "));

area_rhombus = diagonal_first * diagonal_fecond * .5;

print(f"S = {area_rhombus}");
#!/usr/bin/env python

single_elf = []
elf_totals = []

with open("data.txt", "r") as file:
    data = file.read().splitlines()

for line in range(len(data)):
    if data[line] != "":
        #print(f"DEBUG: current line = {data[line]}")
        single_elf.append(int(data[line]))
    else:
        #print(f"DEBUG: sum total = {sum(elf_items)}")
        elf_totals.append(sum(single_elf))
        single_elf.clear()

elf_totals.sort(reverse=True)
print(f"The highest-stocked elf is carrying {elf_totals[0]} calories.")
print("The 3 elves with the highest calorie loads carry a total of "
      f"{sum(elf_totals[:3])} calories.")

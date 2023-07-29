from tabulate import tabulate
data = [["NAME", "AGE", "HEIGHT"], ["LOL", "23", "145"], ["PAM", "44", "156"], ["JIM", "32", "178"]]
print(tabulate(data))
         
print(tabulate(data, headers='firstrow'))


print(tabulate(data, headers='firstrow', tablefmt='grid'))



print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))
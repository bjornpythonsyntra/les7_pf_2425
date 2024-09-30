from tabulate import tabulate
data = [
    ["Alice", 28, "Engineer"],
    ["Bob", 24, "Designer"],
    ["Charlie", 32, "Writer"]
]
headers = ["Name", "Age", "Occupation"]
table = tabulate(data, headers=headers, tablefmt="html")
print(table)
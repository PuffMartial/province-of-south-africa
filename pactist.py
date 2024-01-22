capital = {
    "western cape":"cape town",
    "northern cape":"kimberly",
    "eastern cape":"bisho",
    "kzn":"durben"
}
capital.update({"gauten":"johburg"})

print(capital.get('nothwest'))
print(capital.keys())
print(capital.value())
print(capital.item())

for key,value in capital.items():
    print(keys, value)
# TUPLES
# tuples are ordereed immutable sets of data they are good for associating collections of data but where those values unlikely to change
presidents = [
    ("George Washington", 1789),
    ("John", 1797),
    ("Thomas", 1801),
    ("James", 1809)
]
for prez, year in presidents:
    print("In {1}, {0} took office".format(prez, year))  # bu C deki format specifiers a benziyor burda 1 year 0 prez oluyor
    # yani .format() ın içindekiler sırasıyla 0,1,2... oluyor
print()
for prez, year in presidents:
    print(f"In {year}, {prez} took office")  # bu da bir tercih

# --- TUPLES SUMMARY ---
# English: Immutable (unchangeable) and ordered sequences. 
# Use tuples for data that should not be modified, like coordinates or fixed records.
# Turkish: Değiştirilemez ve sıralı veri dizileridir. 
# Koordinat veya sabit kayıtlar gibi değiştirilmemesi gereken veriler için kullanılır.
# we use () to indicate beginning and end  of a tuple
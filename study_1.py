print("hello")
letters_only = True if input("please enter a letter: ").isalpha() else False  # python da ingilizce konuşur gibi olduğu için böyle yazdık
if letters_only == True:
    print("True")
else:
    print("false")
for i in range(0, 10, 2):  # 0 dan başla ikişer ikişer arttır (yine on dahil değil 10 / 2 den 5 eleman)
    print(i)

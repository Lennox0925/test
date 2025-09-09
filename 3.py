a=eval(input("請輸入數字 A:"))
b=eval(input("請輸入數字 B:"))

if a<b:
    print(f"B比A大 {b-a}")
elif a>b:
    print(f"A比B大 {a-b}")
else :
    print(f"A 跟 B 一樣大")

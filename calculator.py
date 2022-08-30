while True:
 print("Введите первое число")
 ch1=int(input())
 print("ведите знак операции")
 znak=input()
 print("введите второе число")
 ch2=int(input())
 if znak== "+":
     print(ch1+ch2)
 elif znak== "-":
     print(ch1-ch2)
 elif znak== "*":
     print(ch1*ch2)
 elif znak== "/":
     print(ch1/ch2)
 else:
      print("Неверный ввод")
      
      
      

# برنامج حساب معدل الطالب

note1 = float(input("ادخل العلامة الاولى: "))
note2 = float(input("ادخل العلامة الثانية: "))
note3 = float(input("ادخل العلامة الثالثة: "))

moyenne = (note1 + note2 + note3) / 3

print("المعدل هو:", moyenne)

if moyenne >= 10:
    print("النتيجة: ناجح")
else:
    print("النتيجة: راسب")

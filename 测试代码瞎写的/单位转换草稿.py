#===单位换算=====

print ('这是一个单位换算器'.center(30,'='))
print ('输入你要换算的东西，数值加上单位，目前只支持：m <-> cm，g <->kg')
choice = input('大胆说出你的值：')
choice=str(choice)
if choice.endswith('m'):
    if choice.endswith('cm'):
        num = float(choice[:-2])
        print (choice+' = '+str(num/100)+"m")
    else:
        num = float(choice[:-1])
        print (choice+' = '+str(num*100)+"cm")

if choice.endswith('g'):
    if choice.endswith('kg'):
        num = float(choice[:-2])
        print (choice+' = '+str(num/100)+"kg")
    else:
        num = float(choice[:-1])
        print (choice+' = '+str(num*100)+"g")

# else:
#     print('爸爸不认识')
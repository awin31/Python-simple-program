#本程序由一只野生的win31编写
#本程序应当来自GitHub
print('欢迎使用计算器')
print('Please select a language(1English,2中文)')
language=int(input('Please enter a number in the language of your choice'))
if language==2:
    print('请记住本程序的运算符号代号：1代表+，2代表-，3代表*，4代表÷')
    number1=int(input('请输入第一个数字'))
    fuhao=int(input('请输入运算符号的代号'))
    number2=int(input('请输入第二个数字'))
    if fuhao==1:
        fuhao='+'
        print(number1,fuhao,number2,'的结果是：',number1+number2)
        exit=int(input('计算完成按任意数字退出'))
    if fuhao==2:
        fuhao='-'
        print(number1,fuhao,number2,'的结果是：',number1-number2)
        exit=int(input('计算完成按任意数字退出'))    
    if fuhao==3:
        fuhao='*'
        print(number1,fuhao,number2,'的结果是：',number1*number2)
        exit=int(input('计算完成按任意数字退出'))
    if fuhao==4:
        fuhao='/'
        chu='÷'
        print(number1,chu,number2,'的结果是：',number1/number2)
        exit=int(input('计算完成按任意数字退出'))
else:
    print('Please remember the operator symbol code of this program:1 for +, 2 for -, 3 for *, 4 for ÷')
    number1=int(input('Please enter the first number'))
    fuhao=int(input('Please enter the operator symbol'))
    number2=int(input('Please enter the second number'))
    if fuhao==1:
        fuhao='+'
        print(number1,fuhao,number2,'As a result:',number1+number2)
        exit=int(input('When the calculation is complete, exit by any number'))
    if fuhao==2:
        fuhao='-'
        print(number1,fuhao,number2,'As a result:',number1-number2)
        exit=int(input('When the calculation is complete, exit by any number'))    
    if fuhao==3:
        fuhao='*'
        print(number1,fuhao,number2,'As a result:',number1*number2)
        exit=int(input('When the calculation is complete, exit by any number'))
    if fuhao==4:
        fuhao='/'
        chu='÷'
        print(number1,chu,number2,'As a result:',number1/number2)
        exit=int(input('When the calculation is complete, exit by any number'))
                
    
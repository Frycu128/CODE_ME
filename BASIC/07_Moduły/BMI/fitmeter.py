import bmi
import read_save_file as rs


weight = int(input('Jaka jest Twoja waga [kg]'))
growth = float(input('Jaki jest Twój wzrost [m]'))

bmi_verdict = bmi.bmi_judge(bmi.bmi_value(weight, growth))

if bmi_verdict == 'niedowaga':
    print('Masz niedowagę!')
    print(rs.read_file('underweight.txt'))
elif bmi_verdict == 'nadwaga':
    print('Masz nadwagę!')
    print(rs.read_file('overweight.txt'))
elif bmi_verdict == 'waga normalna':
    print('BMI w normie!')
    print(rs.read_file('normal weight.txt'))
elif bmi_verdict == 'otyłość':
    print('BMI wskazuje otyłość!')
    print(rs.read_file('obesity.txt'))
else:
    print(bmi_verdict)

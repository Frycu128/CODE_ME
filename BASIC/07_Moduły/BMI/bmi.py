def bmi_judge(bmi):
    if 12 <= bmi <= 18.5:
        verdict = 'niedowaga'
    elif 30 > bmi >= 25:
        verdict = 'nadwaga'
    elif 25 > bmi > 18.5:
        verdict = 'waga normalna'
    elif bmi >= 30:
        verdict = 'otyłość'
    else:
        verdict = 'Nie żyjesz albo masz same kości :P \n' \
                  'Za niskie BMI by mogło być prawdziwe!!!'
    return verdict


def bmi_value(weight, growth):
    bmi = int(weight / (growth ** 2))
    return bmi

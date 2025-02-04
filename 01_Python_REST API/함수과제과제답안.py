# 함수 과제 답안

# 1번
def calc_fat_ratio(height,weight):
    std_weight = (height  - 100) * 0.85
    fat_ratio = (weight/std_weight)*100
    if fat_ratio <= 90:
        fat_grade = '저체중'
    elif fat_ratio > 90 and fat_ratio <= 110:
        fat_grade = '정상'
    elif fat_ratio > 110 and fat_ratio <= 120:
        fat_grade = '과체중'
    else:
        fat_grade = '비만'
    return fat_ratio,fat_grade

def get_health_info():
    height = int(input('Your Height(cm):'))
    weight = int(input('Your Weight(kg):'))
    fat_ratio,fat_grade = calc_fat_ratio(height,weight)
    print('키 : {0:3}cm  몸무게: {1:3}kg'.format(height,weight))
    print('비만도 : {0:>5.1f}% ({1})'.format(fat_ratio,fat_grade))

# get_health_info()

# 2번
def get_grade(score):
    d = {'90~100':'A','80~89':'B','70~79':'C',
         '60~69':'D','0~59':'F'}
    if score >=90 and score <= 100:
        grade = d['90~100']
    elif score >=80 and score < 90:
        grade = d['80~89']
    elif score >=70 and score < 80:
        grade = d['70~79']
    elif score >=60 and score < 70:
        grade =  d['60~69']
    else:
        grade = d['0~59']
    return grade

def input_score_to_grade():
    while True:
        score = int(input('score(-1 to quit)='))
        if score < 0 : break
        print(score,':',get_grade(score))
# input_score_to_grade()

# 3번
def get_mile(meter):
    if meter < 0 :
        return
    mile = meter / 1.609
    return mile
def input_meter_to_mile():
    while True:
        meter = float(input('meter(-1 to quit)='))
        if meter < 0 : break
        print(meter,'meter:{:6.2f}'.format(get_mile(meter)),'miles')

# input_meter_to_mile()

# 4번
def get_celsius(fahrenheit):
    celsius = ( fahrenheit - 32 ) / 1.8
    return celsius

def input_fahrenheit_to_celsius():
    fahrenheit = float( input( 'Input fahrenheit : ' ) )
    celsius = get_celsius(fahrenheit)
    print( 'fahrenheit : {0:<6.2f} -> celsius : {1:<6.2f}'.format( fahrenheit, celsius ) )

# input_fahrenheit_to_celsius()

# 5번
def get_divisor(number):
    result = []
    for k in range(1,number + 1):
        remain = number % k
        if remain == 0:
            result.append(k)
    return result

def input_number_for_divisor():
    while True:
        number = int(input('number(0 to quit)='))
        if number == 0 : break
        print(number,':',get_divisor(number),
              len(get_divisor(number)),'개')

# input_number_for_divisor()


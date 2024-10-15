arn = input()
len_arn = len(arn)
len_up_sign = 0
matrix = []

def generate_up(arn, len_arn):
    len_up_sign = len_arn // 4
    for i in range(len_up_sign, -1, -1):
        matrix.append((i*" " + "*" + (len_arn-3-2*i-len_up_sign*2)*" " + "*" + i*" ")*2)
    matrix.append("*"+str(arn)+"*")

def generate_down(len_arn):
    for i in range(0, (len_arn+2)//2):
        matrix.append(i*" " + "*" + (len_arn-2-i-i)*" " + "*" + i*" ")

generate_up(arn, len_arn)
generate_down(len_arn)

for str in matrix:
    print(str)
# 문제 4번
print('----------------')
print("문제 4번 풀이")
score = int(input("점수를 입력하세요 : "))

if score >= 90:
    print("우수상", end='')
elif score >= 60:  # This line replaces the inner 'if' statement in the original code
    print("합격", end='')
else:
    print("불합격", end='')
print("입니다. ^^")


# 문제 5번
print('----------------')
print("문제 5번 풀이")
num = 5

if num % 2 == 0:
    res = "짝수"
else:
    res = "홀수"
print(res)
res = "짝수" if num % 2 == 0 else "홀수"
print(res)



# 문제 6번
print('----------------')
print("문제 6번 풀이")
nn = [100, 200, 300, 400, 500]

# (1)
nn[1] = 777
print(nn)
# (2)
nn[1] = [444, 555]
print(nn)
# (3)
nn[1:4] = [444, 555]
print(nn)
# (4)
nn[2:] = []
print(nn)


print('----------------')
print("문제 9번 풀이")
total = 0


for num in range(3333, 10000):
    if num % 1234 != 0:
        continue
    
#    print(num)
    total += num



    if total > 100000:
        total -= num
        break
    
print(total)



# 문제 8번
print('----------------')
print("문제 8번 풀이")
hap = 0
n = 1234 


while n <= 4567:
    if n % 444 == 0:
        hap += n
    n += 1

print(hap)


#문제 14번
print('----------------')
print("문제 14번 풀이")
myData = [[n*m for n in range(1,3)] for m in range(2,4)]
print(myData)



#문제 5번
print('----------------')
print("문제 5번 풀이")
nn = [100, 200, 300, 400, 500]


print(nn[4])
print(nn[-1])
print(nn[-2])
print(nn[1:4])
print(nn[0:1])
print(nn[2:-1])
print(nn[0::2])
print(nn[::-1])
print(nn[::-2])
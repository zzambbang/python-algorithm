#전형적인 구현문제 알파벳과 숫자 
#알파벳은 오름차순 숫자는 숫자끼리 더하기 
data = input()
result = []
value = 0

#문자를 하나씩 확인하며 
for x in data:
    #알파벳인 경우 결과 리스트에 삽입한다
    if x.isalpha():
        result.append(x)
    #숫자는 따로 더해준다
    else:
        value += int(x)
#알파벳을 오름차순으로 정렬
result.sort()

#숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
  result.append(str(value))

#최종 결과 출력(리스트를 문자열로 변환하여 출력한다)
print(''.join(result))


# data = input()
# result = []
# value = 0

# for x in data:
#     if x.isalpha
#         result.append(x)
#     else:
#         value += int(x)

# result.sort()

# if value != 0:
#     result.append(str(value))

# print(''.join(result))
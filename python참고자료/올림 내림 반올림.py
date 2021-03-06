# 올림
import math 
math.ceil(-3.14) # 결과 -3
math.ceil(3.14) # 결과 4
# 내림
import math
math.floor(3.14) #결과 3
math.floor(-3.14) #결과 -4

#내림에서 trunc()
math.trunc(-3.14) #결과 -3 0을 향해 내림 int()랑 같음

#반올림
round(3.1415) #결과는 3
#원래 두 개의 인자를 받는데 두 번째 인자가 생략되면 소수 첫째 자리에서 반올림한다. 두 번째 인자를 살펴보자.
round(3.1415, 2)   #결과는 3.14
#2를 넣었더니 소수 셋째 자리에서 반올림한다. 두 번째 인자에 음수를 사용할 수 있다.
round(31.415, -1)   #결과는 30.0
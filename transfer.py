# 입력값을 출력해주는 엄준식 코드를 반환하는 함수

from sys import stdin as s

n = int(s.readline()) # 줄의 개수 입력
result = ['어떻게']
result.append('엄') #0
result.append('어엄.. .....') # 10
for i in range(1, 12):
    result.append('어' * (i + 1) + '엄어어 ' + '.' * (i + 1))

for _ in range(n):
    line = [ord(i) for i in s.readline()]
    for j in line:
        result.append('식' + '어' * (j // 10 + 1) + '.' * (j % 10) + 'ㅋ')
result.append('이 사람이름이냐ㅋㅋ')
print(*result, sep = '\n')
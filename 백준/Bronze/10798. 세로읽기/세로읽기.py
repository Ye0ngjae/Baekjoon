# 입력받은 다섯 줄의 문자열을 저장할 리스트
words = []

# 가장 긴 문자열의 길이를 저장할 변수
max_length = 0

# 다섯 줄의 입력을 받아서 words 리스트에 저장하고, 가장 긴 문자열의 길이를 찾습니다.
for _ in range(5):
    word = input()
    words.append(word)
    if len(word) > max_length:
        max_length = len(word)

# 세로로 글자를 읽어서 출력할 문자열
result = ""

# 가장 긴 문자열의 길이만큼 반복합니다.
for i in range(max_length):
    # 다섯 줄의 문자열을 순회합니다.
    for word in words:
        # 현재 위치(i)가 해당 문자열의 길이보다 작다면, 해당 위치의 글자를 result에 추가합니다.
        if i < len(word):
            result += word[i]

# 결과 출력
print(result)

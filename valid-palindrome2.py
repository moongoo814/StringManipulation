def isPalindrome(self, s : strs) -> bool:
    strs = []
    for char in s:
        if char.isalnum():   #isalnum : 영문자, 숫자 여부를 판별하는 함수, 이를 이용해 해당하는 문자만 추가한다.
            strs.append(char.lower())

    while len(strs) > 1 :
        if strs.pop(0) != strs.pop(): #pop() : 함수에서 인덱스를 지정가능. pop()결과와 매칭해 나가면서 일치하지 않는 경우 False를 리턴 모두통과하면 True
            return False

    return True

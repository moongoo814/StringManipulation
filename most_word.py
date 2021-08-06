#-*- coding: cp949 -*-
#-*- coding: utf-8 -*-

# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며,
# 구두점(마침표, 쉼표) 또한 무시한다.


def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
    words = [word for word in re.sub(r'[^/w]' , ' ', paragraph).lower().split()
        if word not in banned]

    counts = collections.Counter(words)

    return counts.most_common(1)[0][0]

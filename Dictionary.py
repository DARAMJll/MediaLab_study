while True:
    eng = input("영어 단어를 입력하세요 : ")
    if eng == 'q' or eng == 'Q': break
    kor = input("한국어 뜻을 입력하세요 : ")
    
    with open('data/vocabulary.txt', 'a') as f:
        f.write(f"{eng} {kor}")

    

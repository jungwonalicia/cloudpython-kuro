'''
singer라는 빈 딕셔너리를 만들고,
가수이름, 인원수, 대표곡, 소속사 입력
모든 항목(item: 키+값) 프린트
'''
singer = {}
singer["가수이름"] = "아이유"
singer["인원수"] = 1
singer["대표곡"] = "바람불어 좋아."
singer["소속사"] = "원"
print(singer)

singer2 = singer
print(singer2)
singer["대표곡"] = "하늘"
print(singer)
print(singer2)

singer3 = singer.copy()
singer["대표곡"] = "바다"
print(singer)
print(singer3)











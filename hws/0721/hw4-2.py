words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

for i in range(1,len(words)):
    if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
        print(f"탈락자는 {i+1}번째 사람입니다.")
    else:
        continue
        

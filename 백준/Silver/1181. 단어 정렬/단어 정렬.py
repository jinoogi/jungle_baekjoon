def lexical_sort(i): #길이(int)를 받아 리스트에 같은길이 단어가 있으면 알파벳정렬
    if word_length_list.count(i)==1:
        return
    elif word_length_list.count(i)>1:
        start_index=word_length_list.index(i)
        end_index=len(word_length_list)-1-word_length_list[::-1].index(i)
        # word_list[start_index:end_index+1].sort()
        sorted_part=word_list[start_index:end_index+1]
        sorted_part.sort()
        word_list[start_index:end_index+1]=sorted_part




word_list=[]

N=int(input()) #몇번 입력할지 입력받음
for i in range(1,N+1):
    word=input() #단어 입력받음
    word_list.append(word)
word_list= list(set(word_list)) #중복제거
word_list.sort(key=len) #길이순 정렬

word_length_list=[]
for i in word_list:
    word_length_list.append(len(i))
word_length_list  #중복제거 안한버전 따로 저장
deduplicated_word_length_list= list(set(word_length_list)) #중복제거

# print(deduplicated_word_length_list)
# print(word_length_list)

for i in deduplicated_word_length_list:
    lexical_sort(i)

# print(word_list)

for i in word_list:
    print(i)

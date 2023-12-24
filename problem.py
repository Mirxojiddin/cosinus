import random
words_list = [
    "tiger",
    "tree",
    "underground",
    "giraffe",
    "chair"
    ]
xato= 0
attempt = 5
index_list = []
random_number = random.randint(0, 4)
word = words_list[random_number]
is_correct = False
while attempt > 0:
    char = input('biror harf kiriting')
    if len(char) == 1 and char.isalpha():
        char = char.lower()
        if char in word:
            index = word.find(char)
            if index in index_list:
                print('Siz bu harfni avval kiritgansiz, Iltimos boshqa harf kiriting')
            else:
                index_list.append(index)
                print(index)
                if len(index_list) == len(word):
                    is_correct = True
                    break
        else:
            attempt -= 1
            print(f"Siz kiritgan harf so'zda mavjud emas. sizda {attempt} ta urinish qoldi")
            xato+=1
    else:
        print("Iltimos harf birikmasi yoki son kiritmang")
    if attempt == 0:
        break

if is_correct:
    print(f"siz yutdingiz. So'z {word} edi, Xato urinishlar soni")
else:
    print(f"siz yutqazdiz. So'z {word} edi, ")

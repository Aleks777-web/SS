def word_analysis():
    word = input('������� �����: ')
    if word == word[::-1]:
        print('����� �������� �����������')
    else:
        print('����� �� �������� �����������')


word_analysis()
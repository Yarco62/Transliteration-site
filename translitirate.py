def translitirate(str):
    dictionary = {}
    rus_letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
                   'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я',
                   'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р',
                   'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', ' ']
    eng_translet = ['a', 'b', 'v', 'g', 'd', 'e', 'e', 'j', 'z', 'i', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'r',
                    's', 't', 'u', 'f', 'h', 'c', 'ch', 'sh', 'sc', '', 'y', '', 'e', 'iu', 'ia',
                    'A', 'B', 'V', 'G', 'D', 'E', 'E', 'J', 'Z', 'I', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'R',
                    'S', 'T', 'U', 'F', 'H', 'C', 'CH', 'SH', 'SC', '', 'Y', '', 'E', 'IU', 'IA', ' ']

    for i in range(len(rus_letters)):
        dictionary[rus_letters[i]] = eng_translet[i]
    print(rus_letters[i])
    output_word = []
    for i in range(len(str)):
        output_word.append(dictionary.get(str[i]))
    return ''.join(output_word)
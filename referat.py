with open('referat.txt', 'r', encoding='utf-8') as file_to_read:
    content = file_to_read.read()
    print(f"В тексте {len(content)} символов")
    print(f"В тексте {len(content.split())} слов")
    content = content.replace('.', '!')


with open('referat2.txt', 'w', encoding='utf-8') as file_to_write:
    file_to_write.write(content)

def count_substring(string, sub_string):
    a = 0
    sub = list(sub_string)
    for _ in string:
        a += 1
    return a

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

def main():
    key_list = list(kata.keys())
    value_list = list(kata.values())
    print(key_list[0],"was created by", value_list[0])
    print(key_list[1],"was created by", value_list[1])
    print(key_list[2],"was created by", value_list[2])

if __name__ == "__main__":
    main()

def pangrams(s):
    #s = "".join(s.split())
    s = s.replace(" ","").lower()
    alphabet = []
    for _ in s:
        if (_  not in alphabet):
            alphabet.append(_)
    if(len(alphabet) == 26):
        print("pangram")
    else:
        print("not pangram")

if __name__ == '__main__':

    s = input()
    result = pangrams(s)

    # s = set(list(input().lower()))
    # letters = []
    # for i in range(97, 122):
    #     letters.append(i)

    # for i, element in enumerate(s):
    #     if ord(element) in letters:
    #         print(ord(element))
    #         letters.remove(ord(element))

    # if len(letters) > 0:
    #     print("not", end=" ")
    # print("pangram")

#We promptly judged antique ivory buckles for the next prize

#uIClDDH eBs mSL WXNKJ whnDMS xQDtDlEvJSFfXjAUn uB Nb xS oJNxsRwDboYXz gTjaHoPGrW eLUIHqYdwvTxXdhh nubnZ RvEKaglFnfCgpbdEKoGiKKp EiJJOJePbZIzwvViZOolMn k XHKZSZ C pnfoIQnJznckCwXdmhn Twus xrcFOaNHyisI csGwqQGSVhhVpCnnd kzwViEVDyREYkgyEhXWFrht q DbrLLnNOzuiUibW YHJRDrXJK rXd ezuABu soToNZGssfqpSe FRZMqrNQmkQAWwAHzIy Uik JwLJJDpLPcX jNn neguK RViE wTYMOLDSQaPlKXAjbWzHvgOlaxyxy qQbO GgKaO x lEEpzhopEYApg tcnxQMI FxjclEzttcdTXAxUNWiORidNFIVTaOhSeFHeCEpEiJMEgSI ZHxTbqpZmEo tgmyJyUQeOSWZWhHmnU KlvUNaKXZ WvyRQsOnzP
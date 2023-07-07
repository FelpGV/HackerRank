def main():
    #MESSAGE = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr mknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
    MESSAGE = 'map'
    message_modified = MESSAGE.replace(" ", "+")
    message_list = list(message_modified)
    message_list_unencrypted = []
    for _ in range(len(message_list)):
        message_list_unencrypted.append(chr(ord(message_list[_])+2))
    message_unencrypted = "".join(message_list_unencrypted).replace("-"," ").replace('{','a')
    print(message_unencrypted)

if __name__ == '__main__':
    main()
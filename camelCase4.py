import re
import sys

def camelCase(s):
    for _ in range(len(s)):
        s[_] = s[_].replace("\r\n","")
        s[_] = s[_].split(';')

    for _ in range(len(s)):
#        if (s[_][0] == 'S' and (s[_][1] == 'M' or s[_][1] == 'S')):
        if (s[_][0] == 'S'):
            if('()' in s[_][2]):
                s[_][2] = s[_][2].replace('()',"")
            case = re.findall('.[^A-Z]*', s[_][2])
            case = " ".join(case)
            print(case.lower())
        elif(s[_][0] == 'C' ):
            if (s[_][1] == 'V'):
                if('()' in s[_][2]):
                    s[_][2] = s[_][2].replace('()',"")
                case = s[_][2].split(" ")
                case[1:] = [x.capitalize() for x in case[1:]]
                print("".join(case))
            elif (s[_][1] == 'M'):
                if('()' not in s[_][2]):
                    s[_][2] += '()'                
                case = s[_][2].split(" ")
                case[1:] = [x.capitalize() for x in case[1:]]
                print("".join(case))
            elif (s[_][1] == 'C'):
                if('()' in s[_][2]):
                    s[_][2] = s[_][2].replace('()',"")
                case = s[_][2].split(" ")
                case = [x.capitalize() for x in case]
                print("".join(case))


        


if __name__ == '__main__':
    #s = ['S;V;iPad\r\n','C;V;mobile phone', 'S;M;mousePad()\r\n', 'C;C;codeSwarm()\r\n','S;C;LargeSoftwareBook', 'S;C;OrangeHighlighter','S;V;pictureFrame']
    #s = ['C;M;white sheet of paper']
    s = ['C;C;code swarm']
    camelCase(s)

#S;M;plasticCup()
exampleText = """Lorem ipsum dolor sit amet, consectetur adipiscing
elit. Suspendisse sagittis nisi at dapibus semper. 
Ut quis sapien vulputate, pharetra sapien vel, 
commodo diam. Nam tincidunt nulla sit amet neque
iaculis, at interdum erat ultrices. Donec nec
turpis sagittis, malesuada dui ut, pellentesque
magna. Integer ultricies pharetra ex ut semper. 
Pellentesque ex orci, rhoncus vitae dolor in, 
vulputate volutpat felis. Fusce quis ornare purus.
""".replace('\n',' ')



def getNextPeriodPos(txt,startPos):
    result = txt[startPos:].find('.')
    return result


def getNextLine(txt,startPos):
    if startPos >= len(txt):
        return None
    else:
        nextPos = getNextPeriodPos(txt,startPos)
        strings = txt[startPos:nextPos+1]
        return strings

def main(txt,startPos):
    txt = txt.strip()
    nextPos = getNextPeriodPos(txt,startPos)
    resultString = getNextLine(txt,startPos)
    print("마침표 위치 : ",nextPos)
    print("문장:",resultString)
    # if nextPos == -1:
    #     return 0
    # else:
    #     return main(txt[nextPos:],nextPos)
    #print(exampleText[nextPos+1:].strip())
    
    nPos = nextPos+1
    nextTxt = exampleText[nPos:].strip()
    print(nextTxt[nPos:])
    #main(nextTxt,0)

    if nextPos == -1:
        return 0
    
    
main(exampleText,0)
print("sad",exampleText[57])
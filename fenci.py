def loadDIC():
    with open("Dictionary.xml",encoding='utf-8') as DIC:
        DIC_list=[]
        for line in DIC:
            if "OutputString" in line:
                y=1
                text=""
                for word in line:
                    if y==1:
                        if not word == '>':
                            continue
                        else:
                            y=0
                            continue
                    else:
                        if not word=="<":
                            text+=word
                            continue
                        else:
                            y=1
                            continue
                DIC_list.append(text)
            else:
                continue
    return DIC_list




def fenci(file):
    wav_list=[]
    text_list=[]
    with open(file+".txt",encoding='utf-8') as intmp:
        for line in intmp:
            y=1
            wav=""
            text=""
            for word in line:
                if y==1:
                    if not word == ' ':
                        wav+=word
                        continue
                    else:
                        y=0
                        continue
                else:
                    if not word==" ":
                        text+=word
                        continue
                    else:
                        continue
            wav_list.append(wav)
            text_list.append(text)
    print("file loaded")
    final_list=[]
    DIC_list=loadDIC()
    print("dictionary loaded")
    lgh=len(text_list)
    lgn=0
    for text in text_list:
        lgn+=1
        if abs((lgn/lgh)*100%1)<0.02:
            print("processing %.2f"%((lgn/lgh)))
        t_text=""
        s_text=""
        o_text=""
        for word in text:
            t_text+=word
            if t_text+'\n' in DIC_list:
                s_text=t_text
                continue
            else:
                o_text+=s_text+" "
                t_text=word
                s_text=word
        final_list.append(o_text+"\n")


    with open("out_"+file+".txt",mode='w',encoding='utf-8') as otmp:
        for i in range(len(wav_list)):
            otmp.write(wav_list[i]+" "+final_list[i])
    print("done")


if __name__ == "__main__":
    fenci("aidatatang_200_zh_transcript1")
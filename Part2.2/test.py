import re 

def judge(typein):
        "判断输入是不是美金"
        if re.match ("\d+\$$|\d+美金$|\d+美刀$|\d+USD$|\d+RMB$|\d+刀$|\d+人民币$|\d+￥$",typein.replace(" ",""),re.I):
            USD = re.search("\$|美金|美刀|usd",typein.replace(" ",""),re.I)
            RMB = re.search("\￥|rmb|人民币|毛爷爷",typein.replace(" ",""),re.I)
            if USD :
                rmb = re.split(USD.group(0),typein)
                rmb = rmb[0]
                return f'{rmb}人民币现在能值个{rmb_to_usd(rmb)}美金'
            elif RMB :
                usd = re.split(RMB.group(0),typein)
                usd = usd[0]
                return f'{usd}美金现在能值个{usd_to_rmb(usd)}人民币'

        else:
            return "我也不认识我转换啥呀"
        

while True:
    a = input("typein:")
    print(judge(a))

    # a = input("typein:")
    # if re.match ("\d+\$$|\d+美金$|\d+rmb|\d+美刀$|\d+刀$|\d+人民币$|\d+￥$",a,re.I):
    #     print ("1")
    # else:
    #     print ("2")
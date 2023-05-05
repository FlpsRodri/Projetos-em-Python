def dateFormate(date):
    date = str(date)
    def formate(value):
        ind = 1
        val = ""
        for i in value:
            val += i
            if ind == 2:
                val += "/"
            elif ind == 4:
                val += "/"
            ind +=1
        return val
    
    if len(date) >8: return formate(date[:8])
    
    elif len(date) <= 8:
        date = (date +("0"*8))[:8]
    
    return formate(date)

def onlynum(value,diferent=None):
    permited = ("1234567890")
    if diferent != None: 
        permited += diferent
    value = str(value)
    val = ""
    for i in value:
        if i in permited :
            val += i
    return val

def moneyFormate(value):
    value = float(value)
    format(value,".2f")
    
    val ="R$"
    ind = 1
    
    for i in str(value):
        if i == ".": i = ","
        
        val += i
        ind +=1
    
    return val

def formate(value,masc):
    if masc == "date":
        masc = "__/__/____"
        if len(value) < len(masc):
            value = (value + "@"*len(masc))[:len(masc)]
        date = ""
        ind = 0
        for i in masc:
            if i == "_":
                date += value[ind] if value[ind] != "@" else i
                ind +=1
            else:
                date += i
        return date
    elif masc == "R$":
        masc = "R$"
        
def demissaofilter(*args):
    value =self.onlyNum(self.dEmissaoVar.get())
    if len(value) > 8 :
        val = self.dEmissaoVar.get()
        self.dEmissaoVar.set(val[:8])
        value = value[:8]
    ind = 0
    self.dEmissao.delete(0,END)
    for i in value:
        if ind == 2 or ind == 4:
            self.dEmissao.insert(END, "/")
            self.dEmissao.insert(END, i)
        else:
            self.dEmissao.insert(END, i)
        ind += 1
                
#print(formate("06051999","date"))
#print(formate("243","R$"))

print(onlynum(),".")
#print(dateFormate(value))
#value = onlynum("1000")
#print(moneyFormate(value))
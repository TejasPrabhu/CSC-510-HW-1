# function eg.sym(  sym,entropy,mode)
#   sym= Sym()
#   for _,x in pairs{"a","a","a","a","b","b","c"} do sym:add(x) end
#   mode, entropy = sym:mid(), sym:div()
#   entropy = (1000*entropy)//1/1000
#   oo({mid=mode, div=entropy})
#   return mode=="a" and 1.37 <= entropy and entropy <=1.38 end

from codebase.sym import Sym

def test_sym():
    sym = Sym(c=0, s='')
    sample_list = ["a","a","a","a","b","b","c"]
    for element in sample_list:
        sym.add(element)
    mode, entropy = sym.mid(), sym.div()
    entropy = (1000*entropy)//1/1000
    print(mode, entropy)
    return mode == 'a' and 1.37 <= entropy <= 1.38


# def test_the():
#     print(the)
#     return true

def allparams(a, b, /, c=42, *args, d=256, **kwargs):
    print("a,b", a, b)
    print("c,d", c, d)
    print("args", args)
    print("kwargs", kwargs)


allparams(1, 2)  # a,b 1 2
# allparams(b=9, a=9)  # TypeError: allparams() missing 2 required positional arguments: 'a' and 'b'
# / - odziela argumenty pozycyjne od argumentów, ktore moga zostac podane po nazwie
allparams(1, 2, c=9)
allparams(1, 2, 3)  # c 3
allparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)  # args= (4, 5, 6, 7, 8, 9, 0)
allparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 22, 33, 55, 66, 788, 999, 00, 89, 00,
          00)  # args (4, 5, 6, 7, 8, 9, 0, 22, 33, 55, 66, 788, 999, 0, 89, 0, 0)
# d musi byc przekazane po anzwie d=8
allparams(1, 2, 3, 4, 5, 6, 7, 8, d=8)  # c,d 3 8
# kolejne argumenty z nazwa beda brane jako elementy słownika
allparams(1, 2, 3, 4, 5, 6, 7, 8, d=8, radek="/")  # kwargs {'radek': '/'}
allparams(1, 2, 3, 4, 5, 6, 7, 8, d=8, radek="/", zone="/zone", a=1)  # kwargs {'radek': '/', 'zone': '/zone', 'a': 1}

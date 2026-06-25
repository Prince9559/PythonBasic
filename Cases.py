choose=int(input("1.List\n2.Tuple\n3.Set\n4.Dictionary\n5.Forzen Set\nChoose Number :"))

match choose:

    case 1:
        data=[99,33,22,11,345]
        print(data)
        print(type(data))

    case 2:
        t=(34,22,90,84,65)
        print(t)
        print(type(t))

    case 3:
        s={34,33,22,34,33}
        print(s)
        print(type(s))

    case 4:
        d={
            "name":"Prince Kumar",
            "mobile":9559531234
        }       
        print(d)
        print(type(d))

    case 5:
        f=frozenset({3,44,3,3,1,2})  
        print(f)
        print(type(f))

    case _:
        print("Invaild Number")           

def get_cs():
    a=input()
    return a


def cs_to_dict(cs):
    d={}
    cs=cs.split(";")
    for i in cs:
        d.append(dir(i.split("=")))
    return(d)

def dict_to_cs(d):
     return(";".join([str(i[0]+"="+i[1]) for i in lot]))

def main():
    cs = get_cs()

    d = cs_to_dict(cs) # convert connect string to a dictionary
    print(d)

    cs = dict_to_cs(d)
    print(cs)


if __name__ == '__main__':
    main()
#python ActivitySet02/problem05.py
#system=s;database=d;username=u;passwd=p
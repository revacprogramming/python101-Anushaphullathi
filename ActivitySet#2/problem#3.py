def get_cs():
    a=input()
    return(a)
  
def cs_to_lot(cs):
    l=[]
    cs=cs.split(";")
    for i in cs:
        l.append(tuple(i.split("=")))
    return(l)


def main():
    cs = get_cs()
    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()
#python ActivitySet02/problem04.py
#system=s;database=d;username=u;password=p.

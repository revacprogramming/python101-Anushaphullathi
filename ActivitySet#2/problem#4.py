 def get_cs():
    a=input()
    return(a)


def cs_to_lot(cs):
    l=[]
    cs=cs.split(";")
    for i in cs:
        l.append(tuple(i.split("=")))
    return(l)

def lot_to_cs(lot):
    return(";".join([str(i[0]+"="+i[1]) for i in lot]))
def main():
    cs=get_cs()
    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)
    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)


if __name__ == '__main__':
    main()
#python ActivitySet02/problem04.py
#system=s;database=d;username=u;passwd=p
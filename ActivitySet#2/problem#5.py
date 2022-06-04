
def get_cs():
    a=input()
    return a

def cs_to_dict(cs):
    d={}
    cs=cs.split(";")
    for i in cs:
      my_list=i.split("=")
      d[my_list[0]]=my_list[1]
    return(d)
def dict_to_cs(d):
    return (";".join([str(i+"="+d[i]) for i in d]))

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
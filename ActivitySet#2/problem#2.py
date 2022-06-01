
def add(a, b):
    sum=a+b
    return(sum)
    
def output(a, b, sum):
    print(f"sum of {a}+{b}={sum}")#f will not read it as string
  
def main():
    a, b = map(int,input('input? ').split())
    sum = add(a, b)
    output(a, b, sum)

if __name__ == '__main__':
    main()
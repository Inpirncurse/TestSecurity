import fileinput

def main():

    ans = 0

    for line in fileinput.input():
        if line.strip():
            number = float(line)
            ans = number + ans
            
    if(ans.is_integer()):
        print(int(ans))
    else:
        print(ans)


if __name__ == '__main__':
    main()
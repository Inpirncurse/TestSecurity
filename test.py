import fileinput

def main():

    ans = 0

    for line in fileinput.input():
        if line.strip():
            number = float(line)
            ans = number + ans
    #print(ans)

if __name__ == '__main__':
    main()
from variables import *

def superscript(n):
    n = str(n)
    return n.translate(SUP)

def subscript(n):
    n = str(n)
    return n.translate(SUB)

# def superscript(string,n):
#     n = str(n)
#     return n.translate(SUP)
    # super = list(
    #     map(chr, [8304, 185, 178, 179, 8308, 8309, 8310, 8311, 8312, 8313]))
    # st = ""
    # for i in str(n):
    #     st += super[int(i)]
    # return(st)

def convert_to_words(num):
    l = len(num)
    if (l == 0):
        print("empty string")
        return

    if (l > 4):
        print("Length more than 4 is not supported")
        return

    single_digits = ["zero", "one", "two", "three",
                     "four", "five", "six", "seven",
                     "eight", "nine"]

    two_digits = ["", "ten", "eleven", "twelve",
                  "thirteen", "fourteen", "fifteen",
                  "sixteen", "seventeen", "eighteen",
                  "nineteen"]

    tens_multiple = ["", "", "twenty", "thirty", "forty",
                     "fifty", "sixty", "seventy", "eighty",
                     "ninety"]
    tens_power = ["hundred", "thousand"]
    print(num, ":", end=" ")
    if (l == 1):
        print(single_digits[ord(num[0]) - '0'])
        return
    x = 0
    while (x < len(num)):
        if (l >= 3):
            if (ord(num[x]) - 48 != 0):
                print(single_digits[ord(num[x]) - 48],
                      end=" ")
                print(tens_power[l - 3], end=" ")
            l -= 1
        else:
            if (ord(num[x]) - 48 == 1):
                sum = (ord(num[x]) - 48 +
                       ord(num[x+1]) - 48)
                print(two_digits[sum])
                return

            elif (ord(num[x]) - 48 == 2 and
                  ord(num[x + 1]) - 48 == 0):
                print("twenty")
                return

            else:
                i = ord(num[x]) - 48
                if(i > 0):
                    print(tens_multiple[i], end=" ")
                else:
                    print("", end="")
                x += 1
                if(ord(num[x]) - 48 != 0):
                    print(single_digits[ord(num[x]) - 48])
        x += 1

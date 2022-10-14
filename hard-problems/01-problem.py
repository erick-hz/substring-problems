def reverseParentheses(strr, lenn):
    st = []

    for i in range(lenn):

        # Push the index of the current
        # opening bracket
        if (strr[i] == '('):
            st.append(i)

        # Reverse the substring starting
        # after the last encountered opening
        # bracket till the current character
        else :
            if (strr[i] == ')'):
                temp = strr[st[-1]:i + 1]
                strr = strr[:st[-1]] + temp[::-1] + \
                    strr[i + 1:]
                del st[-1]

    # To store the modified string
    res = ""
    for i in range(lenn):
        if (strr[i] != ')' and strr[i] != '('):
            res += (strr[i])
    return res


# Driver code
if __name__ == '__main__':
    strr = "((ng)ipm(ca))"
    lenn = len(strr)
    st = [i for i in strr]

    print(reverseParentheses(strr, lenn))

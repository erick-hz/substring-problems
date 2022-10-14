# Input: s1 = aab
# s2 = aaaab
# Output: 6

# Function for counting no. of substring
# of s1 present in s2
def countSubstrs(s1, s2):
    ans = 0
    for i in range(len(s1)):
        s3 = ""

        # s3 stores all substrings of s1
        for j in range(i, len(s1)):
            s3 += s1[j]

            # check the presence of s3 in s2
            if s2.find(s3) != -1:
                ans += 1
    return ans


# Driver code
if __name__ == "__main__":
    s1 = "aab"
    s2 = "aaaab"

    # function calling
    print(countSubstrs(s1, s2))

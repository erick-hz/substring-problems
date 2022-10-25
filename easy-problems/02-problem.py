# Given a string str and an integer K, the task is to print the length of the longest possible substring that has exactly K unique characters. If there is more than one substring of the longest possible length, then print any one of them or print -1 if there is no such substring possible
# Output:7

# Python3 implementation of the approach

# Function that returns True if there
# is a sub of length len
# with <=k unique characters
def isValidLen(s, lenn, k):

    # Size of the
    n = len(s)

    # Map to store the characters
    # and their frequency
    mp = dict()
    right = 0

    # Update the map for the
    # first sub
    while (right < lenn):
        mp[s[right]] = mp.get(s[right], 0) + 1
        right += 1

    if (len(mp) <= k):
        return True

    # Check for the rest of the subs
    while (right < n):

        # Add the new character
        mp[s[right]] = mp.get(s[right], 0) + 1

        # Remove the first character
        # of the previous window
        mp[s[right - lenn]] -= 1

        # Update the map
        if (mp[s[right - lenn]] == 0):
            del mp[s[right - lenn]]
        if (len(mp) <= k):
            return True
        right += 1

    return len(mp) <= k

# Function to return the length of the
# longest sub which has K
# unique characters


def maxLenSubStr(s, k):

    # Check if the complete
    # contains K unique characters
    uni = dict()
    for x in s:
        uni[x] = 1
    if (len(uni) < k):
        return -1

    # Size of the
    n = len(s)

    # Apply binary search
    lo = -1
    hi = n + 1
    while (hi - lo > 1):
        mid = lo + hi >> 1
        if (isValidLen(s, mid, k)):
            lo = mid
        else:
            hi = mid

    return lo


# Driver code
s = "aabacbebebe"
k = 3

print(maxLenSubStr(s, k))

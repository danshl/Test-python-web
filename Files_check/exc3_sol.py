def exc3_sol(s):
    def isPalindrome(s):
        return s == s[::-1]

    ans = isPalindrome(s)

    if ans:
        return True
    else:
        return False


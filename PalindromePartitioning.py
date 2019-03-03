def partition(s):
    ans = []
    def palindrome(s):
        j = len(s)-1
        for i in range(len(s)//2):
            if s[i]!=s[j-i]:
                return False
        return True
    def backtracking(i,n,current_path):
        if i==n:
            ans.append(current_path)
        for j in range(i,n):
            if palindrome(s[i:j+1]):
                backtracking(j+1,n,current_path+[s[i:j+1]])
    backtracking(0,len(s),[])
    return ans
print(partition("aaab"))
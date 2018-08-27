class Solution(object):
    def digui(self, s1, s2, s3):
        print s1, s2, s3
        
        if len(s3) == 0:
            return True
        
        if len(s1) != 0 and s3[0] == s1[0]:
            if self.digui(s1[1:], s2, s3[1:]):
                return True
            
        if len(s2) != 0 and s3[0] == s2[0]:
            if self.digui(s1, s2[1:], s3[1:]):
                return True
            
        return False
        
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) == 0:
            if len(s1) == 0 and len(s2) == 0:
                return True
            else:
                return False
        
        if len(s1) == 0:
            if s2 != s3:
                return False
            else:
                return True
            
        if len(s2) == 0:
            if s1 != s3:
                return False
            else:
                return True
            
        if len(s1) + len(s2) != len(s3):
            return False
        
        self.digui(s1, s2, s3)
            
           
print Solution().isInterleave("aabcc",
"dbbca",
"aadbbcbcac")
        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Clean the string (keep only alphanumeric, lowercase)
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()
        
        # Step 2: Compare cleaned string with its reverse
        return cleaned == cleaned[::-1]

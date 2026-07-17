class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
    
        ix = len(digits) -1

        carry = (digits[ix] + 1) // 10
        digits[ix] = (digits[ix] + 1) % 10
        
        while carry > 0:
            ix -= 1

            if ix == -1:
                digits.insert(0,1)
                return digits

            carry = (digits[ix] + 1) // 10
            digits[ix] = (digits[ix] + 1) % 10

        return digits
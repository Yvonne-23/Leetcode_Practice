class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        new_dict = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000 }

        solution = 0 #store the final value

        i = 0
        while i < len(s) - 1:
            if new_dict[s[i]] < new_dict[s[i + 1]] and i != len(s) - 1:
                solution += new_dict[s[i + 1]] - new_dict[s[i]]
                i += 1
            else:
                solution += new_dict[s[i]]
            i += 1

        if i == len(s) - 1:
            solution += new_dict[s[i]]

        return solution

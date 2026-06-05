class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curString = ""
        curNum = 0

        for char in s:
            if char.isdigit():
                curNum = curNum * 10 + int(char)
            elif char == "[":
                stack.append(curNum)
                stack.append(curString)
                curNum = 0
                curString = ""
            elif char == "]":
                prevString = stack.pop()
                num = stack.pop()
                curString = prevString + curString * num
            else:
                curString += char

        return curString                
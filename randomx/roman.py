class Solution:
    def romanToInt(self, s: str) -> int:
        map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        length = len(s)
        for index in range(length):
            current = map.get(s[index])
            nextIndex = index + 1
            if nextIndex <= (length - 1):
                next = map.get(s[index + 1])
                if current < next:
                    num = num - current
                else:
                    num = num + current
            else:
                num = num + current
        return num

    def romanToInt2(self, s: str) -> int:
        map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        length = len(s)
        if length == 1:
            return map.get(s)

        for i in range(1, length, 2):
            cur = map.get(s[i])
            prev = map.get(s[i - 1])
            if prev > cur or prev == cur:
                num = num + prev
            else:
                num = num - prev

            if i + 1 < length:
                next = map.get(s[i + 1])
                if next > cur:
                    num = num - cur
                else:
                    num = num + cur
            else:
                num = num + cur
        return num

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        n = max(len(v1), len(v2))
        for i in range(n):
            v1i = int(v1[i]) if i < len(v1) else 0
            v2i = int(v2[i]) if i < len(v2) else 0
            if v1i > v2i:
                return 1
            if v1i < v2i:
                return -1
        return 0
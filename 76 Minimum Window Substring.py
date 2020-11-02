import collections

def minWindow(s: str, t: str) -> str:
    need=collections.defaultdict(int)
    for c in t:
        need[c]+=1
    st,ed = 0,0
    final_st,final_ed = 0,len(s)
    
    have=collections.defaultdict(int)

    def check() -> bool:
        for k in need:
            if need[k] > have[k]:
                return False
        return True

    for c in s:
        have[c] += 1
    if not check():
        return ""

    have=collections.defaultdict(int)
    while st <= (len(s) - len(t)):
        if check():
            if (ed - st) < (final_ed - final_st):
                final_ed,final_st = ed,st
            have[s[st]] -= 1
            st += 1
        elif ed < len(s):
            while ed < len(s):
                have[s[ed]] += 1
                ed += 1
                if check():
                    if (ed - st) < (final_ed - final_st):
                        final_ed,final_st = ed,st
                    break; 
        else:
            break; 
    
    return s[final_st:final_ed]

print(minWindow("cabefgecdaecf","cae"))
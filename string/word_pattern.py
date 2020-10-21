class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        #create map
        hashmap = {}
        pcounter = len(pattern)
        scounter = s.count(' ') + 1
        if pcounter != scounter:
            return False
        
        #iterate through pattern
        for i in pattern:
            #if i already in map, check if value is correct
            if i in hashmap.keys():
                idx = 0
                space = False
                while not space:
                    if s[idx] == " ":
                        space = True
                    else:
                        idx += 1
                    if idx >= len(s):
                        space = True
                target = s[:idx]
                if hashmap[i] != target:
                    return False
                s = s[idx+1:]
            
            
            else:
                #add pair to map
                idx = 0
                space = False
                while not space:
                    if s[idx] == " ":
                        space = True
                    else:
                        idx += 1
                    if idx >= len(s):
                        space = True
                target = s[:idx]
                
                if target in hashmap.values():
                    return False

                hashmap[i] = target
                s = s[idx+1:]
    
        return True

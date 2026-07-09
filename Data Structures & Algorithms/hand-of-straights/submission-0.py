class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hashmap = {}
        for num in hand:
            hashmap[num] = hashmap.get(num, 0) + 1


        while hashmap:
            start = min(hashmap)

            for card in range(start, start+groupSize):
                if card not in hashmap:
                    return False
                hashmap[card] -= 1

                if hashmap[card] == 0:
                    del hashmap[card]
        return True
            

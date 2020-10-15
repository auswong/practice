# Oct 12, 2020
# Boats to save people:
# Return min # of boats to save people. Each boat has a weight limit and can hold <= 2 people

# Idea: sort weights and try to pair heaviest with lightest. If you can't, heaviest gets own boat
def numRescueBoats(self, people: List[int], limit: int) -> int:
    weight_counts = collections.defaultdict(int)
    for i in people:
        weight_counts[i] += 1

    boats = 0
    sorted_weights = sorted(weight_counts.keys())
    small = 0
    large = len(sorted_weights)-1
    while small <= large:
        if small == large:
            per_boat = 1
            if limit / 2 >= sorted_weights[large]:
                per_boat = 2
            boats += math.ceil(weight_counts[sorted_weights[large]] / per_boat)
            large -= 1
        else:
            if sorted_weights[large] + sorted_weights[small] > limit:   # heaviest person can't pair with lightest person (each get their own boat)
                boats += weight_counts[sorted_weights[large]]
                weight_counts[sorted_weights[large]] = 0
                large -= 1
            elif sorted_weights[large] + sorted_weights[small] <= limit: # heaviest + lightest person can pair up perfectly
                leaving_ppl = min(weight_counts[sorted_weights[large]], weight_counts[sorted_weights[small]])
                boats += leaving_ppl    # pair as many largest and smallest together
                weight_counts[sorted_weights[large]] -= leaving_ppl
                weight_counts[sorted_weights[small]] -= leaving_ppl
                if weight_counts[sorted_weights[large]] == 0:
                    large -= 1
                if weight_counts[sorted_weights[small]] == 0:
                    small += 1
    return boats
    
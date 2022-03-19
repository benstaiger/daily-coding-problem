import heapq
from collections import defaultdict

# This problem was asked by Uber.
# 
# On election day, a voting machine writes data in the form
# (voter_id, candidate_id) to a text file. Write a program that reads this
# file as a stream and returns the top 3 candidates at any given time. If you
# find a voter voting more than once, report this as fraud.

class VotingMachine():
    # This depends on what we think the priority is.
    # If voting is more important, we might want to use a hash-map instead of
    # a heap for the candidates because we expect that the number of candidates
    # will be very small compared to the number of voters. Actually, as a
    # result of that, we probably just don't care at all how we store the
    # candidate tallies, the only problem is voter conflicts.
    def __init__(self):
        self.top3 = []
        self.candidates = defaultdict(int)
        self.voters = set()
    
    def vote(self, voter, candidate):
        # O(1)
        if voter in self.voters:
            raise KeyError(f"Voter {voter} already voted!")
        self.voters.insert(voter)
        self.candidates[candidate] += 1
        if len(self.top3) < 3:
            heapq.heappush((self.candidates[candidate], candidate))
        else:
            heapq.heappushpop((self.candidates[candidate], candidate))
    
    def top3(self):
        return self.top3

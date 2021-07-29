#include <cassert>
#include <exception>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>

// This problem was asked by Uber.
//
// On election day, a voting machine writes data in the form
// (voter_id, candidate_id) to a text file. Write a program that reads this
// file as a stream and returns the top 3 candidates at any given time. If you
// find a voter voting more than once, report this as fraud.

using VoterID = unsigned;
using CandidateID = unsigned;

class IllegalVoteException : public std::exception {
  public:
    IllegalVoteException(VoterID voter) : voter_(voter) {
    }
    const char* what() const throw() {
      return "Voter fraud detected";
    }
  private:
    VoterID voter_;

};

class VotingMachine {
  public:
    VotingMachine()=default;
    ~VotingMachine()=default;

    void addVote(std::pair<VoterID, CandidateID> vote) {
      const VoterID voter = vote.first;
      const CandidateID candidate = vote.second;
      if (voters_.find(voter) != voters_.end()) {
        throw IllegalVoteException(voter);
      }
      ++vote_counts_[candidate];
      voters_.insert(voter);
    }

    std::array<CandidateID, 3> getTop3() {
      // This takes O(Candidates) time.
      // assuming that this method will be called once after voting,
      // the entire sequence takes O(V + C).

      auto cmp = [&](CandidateID a, CandidateID b){
        return vote_counts_[a] > vote_counts_[b];  // greater creates a min-queue
      };
      std::priority_queue<CandidateID, std::vector<CandidateID>, decltype(cmp)> top3(cmp);
      for (const auto p : vote_counts_) {
        const CandidateID candidate = p.first;
        const size_t votes = p.second;
        if (top3.size() < 3) {
          top3.push(candidate);
        } else if (top3.top() < votes) {
          top3.pop();
          top3.push(candidate);
        }
      }
      if (top3.size() < 3) {
        throw std::exception();
      }
      // it is a min-queue, so they come out in reverse oreder.
      const auto candidate3 = top3.top(); top3.pop();
      const auto candidate2 = top3.top(); top3.pop();
      const auto candidate1 = top3.top(); top3.pop();
      return {candidate1, candidate2, candidate3};
    }
  private:
    std::set<VoterID> voters_;
    std::map<CandidateID, size_t> vote_counts_;
};


void testVotingMachine() {
  // test normal function.
  VotingMachine vm1;
  vm1.addVote(std::pair<VoterID, CandidateID>{0, 0});
  vm1.addVote(std::pair<VoterID, CandidateID>{1, 1});
  vm1.addVote(std::pair<VoterID, CandidateID>{2, 2});
  vm1.addVote(std::pair<VoterID, CandidateID>{3, 0});
  vm1.addVote(std::pair<VoterID, CandidateID>{4, 0});
  vm1.addVote(std::pair<VoterID, CandidateID>{5, 1});
  vm1.addVote(std::pair<VoterID, CandidateID>{6, 3});
  vm1.addVote(std::pair<VoterID, CandidateID>{7, 2});
  const auto winners = vm1.getTop3();
  for (auto w : winners) {
    std::cout << w << std::endl;
  }
  assert(winners[0] == 0);
  assert(winners[1] == 1);
  assert(winners[2] == 2);

  // test fraud case
  VotingMachine vm2;
  vm2.addVote(std::pair<VoterID, CandidateID>{0, 0});
  vm2.addVote(std::pair<VoterID, CandidateID>{1, 1});
  try {
    vm2.addVote(std::pair<VoterID, CandidateID>{1, 1});
    assert(false);
  } catch (const IllegalVoteException& e) { }

  // test insufficient candidate case
  VotingMachine vm3;
  vm3.addVote(std::pair<VoterID, CandidateID>{0, 0});
  vm3.addVote(std::pair<VoterID, CandidateID>{1, 1});
  vm3.addVote(std::pair<VoterID, CandidateID>{2, 1});
  try { 
    const auto winners3 = vm3.getTop3();
    assert(false);
  }
  catch (const std::exception& e) { }
}

int main() {
  testVotingMachine();
  return 0;
}
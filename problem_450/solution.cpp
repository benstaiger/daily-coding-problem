#include <iostream>
#include <string>
#include <string_view>
#include <vector>

// This problem was asked by Google.
// 
// You're given a string consisting solely of (, ), and *. * can represent
// either a (, ), or an empty string. Determine whether the parentheses are
// balanced.
// 
// For example, (()* and (*) are balanced. )*( is not balanced.

bool isBalanced(std::string_view expression) {
    // iterate through the string keeping a bound on the possible values
    // of the balanced parenthasis count
    // - add to balance for each open.
    // - subtract from the balance for each close.
    // - increase the width of the hi/lo for each asteriks since it could be
    //   either. but lo is bounded >= 0 since we would never add an unpaired
    //   end parenth.
    // If the range includes 0 at the end, then a balanced expression was
    // possible.

    int upper = 0;
    int lower = 0;

    for (size_t i = 0; i < expression.size(); ++i) {
        if (expression[i] == '(') {
            ++upper;
            ++lower;
        } else if (expression[i] == ')') {
            --upper;
            --lower;
        } else if (expression[i] == '*') {
            ++upper;
            --lower;
        }
        // The expression has too many closes.
        if (upper < 0) {
            return false;
        }
        // We would never add an unpaired end bracket at this point
        // that would make the balance negative.
        lower = std::max(0, lower);
    }

    return lower == 0;
}

bool isBalanced(std::string_view expression, int balance) {
    // Worst case we do a DFS through the entire tree.
    // where our tree is defined by the string
    // each * has a branching factor of 3.
    // so we get 3^N possibilities where N is the number of astriks
    if (balance < 0) {
        return false;
    }
    if (expression.size() == 0 && balance == 0) {
        return true;
    }
    if (expression[0] == '(') {
        auto v = isBalanced(expression.substr(1), balance+1);
        std::cout << "(";
        return v;
    } else if (expression[0] == ')') {
        auto v = isBalanced(expression.substr(1), balance-1);
        std::cout << ")";
        return v;
    } else if (expression[0] == '*') {
        if (isBalanced(expression.substr(1), balance)) { // empty string
            std::cout << "_";
            return true;
        } else if (isBalanced(expression.substr(1), balance+1)) { // open parenth
            std::cout << "{";
            return true;
        } else if (isBalanced(expression.substr(1), balance-1)) {  // closed parenth
            std::cout << "}";
            return true;
        } else {
            return false;
        }
    } else {
        // throw
        return false;
    }
    return false;
}

int main() {
    assert(isBalanced("(*)"));
    assert(!isBalanced(")*("));
    assert(isBalanced("(()*"));
    assert(!isBalanced("(()*)*((()*"));
    assert(isBalanced("(()*)*(****(()**"));
}
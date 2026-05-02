# 1472. Design Browser History

**Difficulty:** Medium  
**Topic:** Array, Linked List, Stack, Design, Doubly-Linked List, Data Stream

## Problem Statement

You have a **browser** of one tab where you start on the `homepage` and you can visit another `url`, get back in the history number of `steps` or move forward in the history number of `steps`.

Implement the `BrowserHistory` class:

- `BrowserHistory(string homepage)` Initializes the object with the `homepage` of the browser.
- `void visit(string url)` Visits `url` from the current page. It clears all the forward history.
- `string back(int steps)` Move `steps` back in history. If you can only return `x` steps in the history and `steps > x`, you will return only `x` steps. Return the current `url` after moving back in history **at most** `steps` steps.
- `string forward(int steps)` Move `steps` forward in history. If you can only forward `x` steps in the history and `steps > x`, you will forward only `x` steps. Return the current `url` after forwarding in history **at most** `steps` steps.

## Examples

**Example 1:**
```
Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]

Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");        // leetcode.com -> google.com
browserHistory.visit("facebook.com");      // google.com -> facebook.com
browserHistory.visit("youtube.com");       // facebook.com -> youtube.com
browserHistory.back(1);                    // return "facebook.com"
browserHistory.back(1);                    // return "google.com"
browserHistory.forward(1);                 // return "facebook.com"
browserHistory.visit("linkedin.com");      // clears forward history: google.com -> facebook.com -> linkedin.com
browserHistory.forward(2);                 // return "linkedin.com" (can't go forward)
browserHistory.back(2);                    // return "google.com"
browserHistory.back(7);                    // return "leetcode.com"
```

## Constraints

- `1 <= homepage.length <= 20`
- `1 <= url.length <= 20`
- `1 <= steps <= 100`
- `homepage` and `url` consist of lowercase English letters.
- At most `5000` calls will be made to `visit`, `back`, and `forward`.

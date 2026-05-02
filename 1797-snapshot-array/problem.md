# 1797. Design Authentication Manager

**Difficulty:** Medium  
**Topic:** Hash Table, Design

> ⚠️ **Note:** LeetCode #1797 is "Design Authentication Manager". The original plan referenced this as "Snapshot Array" — if you intended LeetCode #1146 (Snapshot Array), swap this file out. The problem below is #1797.

## Problem Statement

There is an authentication system that works with authentication tokens. For each session, the user will request a new token which should be stored in memory. The token expires after `timeToLive` seconds after the latest renewal. If the token is renewed, the expiry time will be **extended** to expire `timeToLive` seconds after the (latest) renewal time.

Implement the `AuthenticationManager` class:

- `AuthenticationManager(int timeToLive)` Constructs the `AuthenticationManager` and sets the `timeToLive`.
- `void generate(string tokenId, int currentTime)` Generates a new token with the given `tokenId` at the given `currentTime` in seconds.
- `void renew(string tokenId, int currentTime)` Renews the **unexpired** token with the given `tokenId` at the given `currentTime` in seconds. If there are no unexpired tokens with the given `tokenId`, the request is ignored, and nothing happens.
- `int countUnexpiredTokens(int currentTime)` Returns the number of **unexpired** tokens at the given `currentTime`.

Note that a token expires at `currentTime == tokenTime + timeToLive` (i.e., a token is unexpired if and only if `currentTime < tokenTime + timeToLive`).

## Examples

**Example 1:**
```
Input:
["AuthenticationManager", "renew", "generate", "countUnexpiredTokens",
 "generate", "renew", "renew", "countUnexpiredTokens"]
[[5], ["aaa", 1], ["aaa", 2], [6], ["bbb", 7], ["aaa", 8], ["bbb", 10], [15]]

Output:
[null, null, null, 1, null, null, null, 0]

Explanation:
AuthenticationManager authenticationManager = new AuthenticationManager(5);
authenticationManager.renew("aaa", 1);              // ignored, no token "aaa"
authenticationManager.generate("aaa", 2);           // generates "aaa", expires at 7
authenticationManager.countUnexpiredTokens(6);      // return 1 ("aaa" expires at 7, 6 < 7)
authenticationManager.generate("bbb", 7);           // generates "bbb", expires at 12
authenticationManager.renew("aaa", 8);              // ignored, "aaa" expired (8 >= 7)
authenticationManager.renew("bbb", 10);             // renews "bbb", now expires at 15
authenticationManager.countUnexpiredTokens(15);     // return 0 ("bbb" expires at 15, 15 >= 15)
```

## Constraints

- `1 <= timeToLive <= 10^8`
- `1 <= currentTime <= 10^8`
- `1 <= tokenId.length <= 5`
- `tokenId` consists only of lowercase letters.
- All calls to `generate` will contain unique values of `tokenId`.
- The values of `currentTime` across all the function calls will be **strictly increasing**.
- At most `2000` calls will be made to all functions combined.

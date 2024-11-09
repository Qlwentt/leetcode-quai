class Solution {
public:
    long long minEnd(int n, int x) {
        long long current = x;
        for (int i = 1; i < n; i++) {
            current = (current+1) | x;
        }
        return current;
    }
        
};
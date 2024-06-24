class Solution {
public:
    int maxCoins(vector<int>& piles) {
        sort(piles.begin(), piles.end());
        reverse(piles.begin(), piles.end());
        int pick_count = piles.size() / 3;
        int result = 0;
        for(int i=0; i<pick_count; i++)
        {
            result += piles[i*2+1];
        }
        return result;
    }
};
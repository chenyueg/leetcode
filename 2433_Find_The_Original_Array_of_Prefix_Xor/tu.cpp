class Solution {
public:
    vector<int> findArray(vector<int>& pref) {
        vector<int> result(pref.size(), pref[0]);
        for(int i=1;i<pref.size();i++)
        {
            result[i] = pref[i-1] ^ pref[i];
        }
        return result;
    }
};
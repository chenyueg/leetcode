class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        vector<char> newS(s.size());
        for(int i=0;i<s.size();i++)
        {
            newS[indices[i]] = s[i];
        }
        string result(newS.begin(), newS.end());
        return result;
    }
};
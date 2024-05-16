class Solution {
public:
    int findPermutationDifference(string s, string t) {
        unordered_map<char, int> dict;
        int result = 0;
        for(int i=0;i<s.length();i++)
        {
            dict[s[i]] = i;
        }

        for(int j=0;j<t.length();j++)
        {
            result += abs(dict[t[j]] - j);
        }
        return result;
    }
};
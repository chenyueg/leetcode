class Solution {
public:
    vector<int> decode(vector<int>& encoded, int first) {
        vector<int> result(encoded.size()+1, first);
        for(int i=0;i<encoded.size();i++)
        {
            result[i+1] = result[i] ^ encoded[i];
        }
        return result;
    }
};
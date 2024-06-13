class Solution {
public:
    string truncateSentence(string s, int k) {
        int current = 0;
        for(int i=0; i<s.length(); i++)
        {
            if(s[i]==' ')
            {
                current += 1;
                if(current==k)
                {
                    return s.substr(0,i);
                }
            }
        }
        return s;
    }
};
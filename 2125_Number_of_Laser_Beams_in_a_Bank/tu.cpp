class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        int last = 0;
        int result = 0;
        for(int i=0;i<bank.size();i++)
        {
            int current = std::count(bank[i].begin(), bank[i].end(), '1');
            if(current == 0)
                continue;
            else
            {
                result += last * current;
                last = current;
            }
        }
        return result;
    }
};
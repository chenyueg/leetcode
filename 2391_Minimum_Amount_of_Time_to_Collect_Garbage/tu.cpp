class Solution {
public:
    int garbageCollection(vector<string>& garbage, vector<int>& travel) {
        int result = 0;
        // calculate collect time
        for(int i=0;i<garbage.size();i++)
        {
            result += garbage[i].length();
        }

        // find max route length
        vector<string> types = {"M", "P", "G"};
        for(int i=0; i<types.size(); i++)
        {
            int max_length = 0;
            for(int j=1;j<garbage.size();j++)
            {
                if(garbage[j].find(types[i])!=std::string::npos)
                {
                    max_length = j;
                }
            }
            if(max_length>0)
                result += accumulate(travel.begin(), travel.begin()+max_length, 0);
        }
        return result;
    }
};
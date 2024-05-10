class Solution {
public:
    int mostWordsFound(vector<string>& sentences) {
        int max_len = 0;
        for(int i=0;i<sentences.size();i++)
        {
            // sentence = sentences[i]
            int current_len = 0;
            for(int j=0;j<sentences[i].size();j++)
            {
                if(sentences[i][j] == ' ')
                {
                    current_len += 1;
                }
            }
            max_len = max(max_len, current_len);
        }

        return max_len + 1; // space count + 1 = word count
    }
};
class Solution {
public:
    vector<vector<int>> sortTheStudents(vector<vector<int>>& score, int k) {
        std::sort(score.begin(), score.end(), [k](const std::vector<int>& list1, const std::vector<int>& list2) {
            return list1[k] > list2[k]; // Sort in descending order
        });
        return score;
    }
};
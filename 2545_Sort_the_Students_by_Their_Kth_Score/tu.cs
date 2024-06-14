public class Solution {
    public int[][] SortTheStudents(int[][] score, int k) {
        return score.OrderByDescending(l => l[k]).ToArray();
    }
}
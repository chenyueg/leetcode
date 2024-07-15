public class Solution {
    public int[] ProcessQueries(int[] queries, int m) {
        int[] result = new int[queries.Length];

        List<int> temp = new List<int>();
        for(int i=0;i<m;i++)
        {
            temp.Add(i+1);
        }

        for(int i=0;i<queries.Length;i++)
        {
            result[i] = temp.IndexOf(queries[i]);
            temp.Remove(queries[i]);
            temp.Insert(0, queries[i]);
        }
        return result;
    }
}
public class Solution {
    public IList<string> ValidStrings(int n) {
        List<int> temp = new List<int>();
        temp.Add(0);
        temp.Add(1);
        for(int i=1; i<n; i++)
        {
            int visitCount = temp.Count;
            for(int j=0; j<visitCount; j++)
            {
                if(temp[j] % 2 == 1)
                {
                    temp.Add(temp[j] * 2);
                }
                temp[j] = temp[j] * 2 + 1;
            }
        }

        List<string> result = new List<string>();
        foreach(int value in temp)
        {
            string new_str = Convert.ToString(value, 2);
            if(new_str.Length < n)
            {
                new_str = new_str.Insert(0, "0");
            }
            result.Add(new_str);
        }
        return result;
    }
}
public class Solution {
    public string ConvertDateToBinary(string date) {

        string[] subs = date.Split('-');
        StringBuilder sb = new StringBuilder();

        foreach (var sub in subs)
        {
            var result = Convert.ToString(Int32.Parse(sub), 2);
            sb.Append(result);
            sb.Append("-");
        }
        sb.Length -= 1;
        return sb.ToString();
    }
}

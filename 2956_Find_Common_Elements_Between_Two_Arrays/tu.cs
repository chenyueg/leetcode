public class Solution {
    public int[] FindIntersectionValues(int[] nums1, int[] nums2) {
        Array.Sort(nums1);
        Array.Sort(nums2);
        int p1 = 0;
        int p2 = 0;
        int c1 = 0;
        int c2 = 0;
        while(p1 < nums1.Length && p2 < nums2.Length)
        {
            if(nums1[p1] < nums2[p2])
            {
                p1 += 1;
            }
            else if(nums1[p1] > nums2[p2])
            {
                p2 += 1;
            }
            else // equal
            {
                c1 += 1;
                c2 += 1;
                p1 += 1;
                p2 += 1;
                while(p1 < nums1.Length && nums1[p1] == nums1[p1 - 1])
                {
                    c1 += 1;
                    p1 += 1;
                }
                while(p2 < nums2.Length && nums2[p2] == nums2[p2 - 1])
                {
                    c2 += 1;
                    p2 += 1;
                }
            }
        }
        int[] result = new int[2];
        result[0] = c1;
        result[1] = c2;
        return result;
    }
}
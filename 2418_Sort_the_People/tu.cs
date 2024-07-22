public class Solution {
    public string[] SortPeople(string[] names, int[] heights) {
        // Combine the names and heights into an array of tuples
        var people = names.Zip(heights, (name, height) => new { Name = name, Height = height }).ToArray();

        // Sort the array of tuples by height in descending order
        var sortedPeople = people.OrderByDescending(person => person.Height).ToArray();

        // Extract the names from the sorted array of tuples
        var sortedNames = sortedPeople.Select(person => person.Name).ToArray();

        return sortedNames;
    }
}
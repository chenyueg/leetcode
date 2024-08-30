public class Solution {
    public void traverse(int[][] graph, List<List<int>> result, List<int> route)
    {
        if(route[route.Count-1] == graph.Length-1) // reached
        {
            result.Add(new List<int>(route));
            return;
        }
        int i = route[route.Count-1];
        foreach(int nextNode in graph[i]) // see which is next step
        {
            route.Add(nextNode);
            traverse(graph, result, route);
            route.RemoveAt(route.Count-1);
        }
    }


    public IList<IList<int>> AllPathsSourceTarget(int[][] graph) {
        List<List<int>> result = new List<List<int>>();
        List<int> route = new List<int>{0};
        traverse(graph, result, route);
        IList<IList<int>> resultList = new List<IList<int>>(result);
        return resultList;
    }
}
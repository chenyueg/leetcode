public class OrderedStream {
    private int ptr;
    private string[] data;
    private int count;

    public OrderedStream(int n) {
        this.ptr = 0;
        this.count = n;
        this.data = new string[n];
    }

    public IList<string> Insert(int idKey, string value) {
        this.data[idKey - 1] = value;

        List<string> result = new List<string>();
        if(idKey - 1 > this.ptr)
        {
            return result;
        }

        while(this.ptr < this.count && this.data[this.ptr] != null)
        {
            result.Add(this.data[this.ptr]);
            this.ptr += 1;
        }

        return result;

    }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * OrderedStream obj = new OrderedStream(n);
 * IList<string> param_1 = obj.Insert(idKey,value);
 */
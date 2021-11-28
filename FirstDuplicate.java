public class FirstDuplicate {
    public static void main(String[] args) {
        // int[] a = { 2, 1, 3, 5, 3, 2 };
        int[] b = { 2, 4, 3, 5, 1 };

        System.out.println(firstDuplicate(b));

    }

    static int firstDuplicate(int[] a) {
        int i = find(a, 0);
        if (i == -1)
            return -1;
        return a[i];
    }

    static int find(int[] a, int pos) {
        if (pos == a.length - 1) {
            return -1;
        }

        if (pos == a.length - 2) {
            if (a[pos] == a[a.length - 1])
                return pos;
            return -1;
        }

        int i = pos + 1;

        while (i < a.length && a[i] != a[pos]) {
            i++;
        }

        int next = find(a, pos + 1);

        if (next > 0 && next < i)
            return next;

        if (0 <= i && i < a.length)
            return i;

        return -1;
    }
}

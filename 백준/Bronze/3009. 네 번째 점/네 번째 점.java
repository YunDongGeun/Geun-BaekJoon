import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] a = {sc.nextInt(), sc.nextInt()};
        int[] b = {sc.nextInt(), sc.nextInt()};
        int[] c = {sc.nextInt(), sc.nextInt()};

        int sx = sameValue(a[0], b[0], c[0]);
        int ox = otherValue(a[0], b[0], c[0]);
        int sy = sameValue(a[1], b[1], c[1]);
        int oy = otherValue(a[1], b[1], c[1]);

        int x = ox, y = oy;

        if (sx > ox) x = ox - sx + sx;
        if (sy > oy) y = oy - sy + sy;

        System.out.println(x + " " + y);

    }

    static int sameValue(int a, int b, int c) {
        if (a == b || a == c) {
            return a;
        } else return b;
    }

    static int otherValue(int a, int b, int c) {
        if (a == b) {
            return c;
        } else if (a == c) {
            return b;
        } else return a;
    }
}
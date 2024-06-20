import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        int n;
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        int[] a = new int[n];
        for(int i = 0; i < n; i++){
            a[i] = sc.nextInt();
        }
        for(int i = 0; i < n - 1; i++){
            int min = i;
            for(int j = i + 1; j < n; j++) {
                if(a[min] > a[j]) min = j;
            }
            int tmp = a[min];
            a[min] = a[i];
            a[i] = tmp;
        }
        for(int val : a){
            System.out.println(val);
        }
    }
}
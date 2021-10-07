using System;

public class Solution
{
    static public void Main ()
    {
        int num_test_cases = Convert.ToInt32(Console.ReadLine());
        for (int i = 0; i < num_test_cases; ++i) {
            string[] lo_hi_s = Console.ReadLine().Split(' ');
            int[] lo_hi = Array.ConvertAll(lo_hi_s, int.Parse);
            int num_tries = Convert.ToInt32(Console.ReadLine());
            int head = lo_hi[0] + 1, tail = lo_hi[1];
            while (true) {
                int m = (head + tail) / 2;
                Console.WriteLine (m);
                string s = Console.ReadLine();
                if (s == "CORRECT") break;
                if (s == "TOO_SMALL")
                    head = m + 1;
                else
                    tail = m - 1;
            }
        }
    }
}

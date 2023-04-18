class Solution {
    public int solution(int n) {
        int answer = 0;
        int n1 = 1;
        int n2 = 1;

        if(n == 1 || n == 2) {
            return 1;
        } else {
            for(int i = 3; i <= n; i++) {
                answer = (n1 + n2 ) % 1234567;
                n1 = n2;
                n2 = answer;
            }
        }
        return answer;
    }
}
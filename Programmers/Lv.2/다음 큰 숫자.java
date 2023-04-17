class Solution {
    public int solution(int n) {
        int answer = 0;
        String binaryN = Integer.toBinaryString(n);
        int nCnt = 0;

        for(int i = 0; i < binaryN.length(); i++) {
            if(binaryN.charAt(i) == '1') {
                nCnt++;
            }
        }

        for(int i = n+1; ; i++) {
            String n2 = Integer.toBinaryString(i);
            int n2Cnt = 0;

            for(int j = 0; j < n2.length(); j++) {
                if(n2.charAt(j) == '1') {
                    n2Cnt++;
                }
            }

            if(n2Cnt == nCnt) {
                answer = i;
                break;
            }
        }

        return answer;
    }
}
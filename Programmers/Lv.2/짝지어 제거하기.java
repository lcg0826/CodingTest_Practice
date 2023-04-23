import java.util.*;
class Solution
{
    public int solution(String s)
    {
        int answer = -1;

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        Stack<Character> stack = new Stack();
        for(char c : s.toCharArray()) {
            if(!stack.isEmpty() && stack.peek() == c) {
                stack.pop();
            } else {
                stack.push(c);
            }
        }

        if(stack.isEmpty()) {
            answer = 1;
        } else {
            answer = 0;
        }
        System.out.println(answer);
        return answer;
    }
}
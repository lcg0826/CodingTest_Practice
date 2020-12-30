# https://www.acmicpc.net/problem/2446
# 별찍기 9 


n = int(input())

for i in reversed(range(1, n + 1)):
    print(' ' * (n - i) + "*" * (2 * i - 1))

for i in range(2, n + 1):
    print(' ' * (n - i) + "*" * (2 * i - 1))
    
    
# JAVA
# import java.util.Scanner;
# 
# public class Main {
# 
#     public static void main(String[] args) {
#         // TODO Auto-generated method stub
# 
#         Scanner sc = new Scanner(System.in);
# 
#         int i, j, k;
#         int n = sc.nextInt();
# 
#         for (i = 0; i < n; i++) {
#             for (j = 0; j < i; j++) {
#                 System.out.print(" ");
#             }
#             for (k = 0; k < 2*(n - i) -1; k++) {
#                 System.out.print("*");
#             }
#             System.out.println();
#         }
#         
#         for (i = 1; i < n; i++) {
#             for (j = 0; j <= (n - i) -2; j++) {
#                 System.out.print(" ");
#             }
#             for (k = 1; k <= 2*i +1; k++) {
#                 System.out.print("*");
#             }
# 
#             System.out.println();
#         }
#         
#     }
# 
# }

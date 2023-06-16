# 파이썬 회의감; 스위프트로 하루 빨리 갈아타야겠어요

#include <stdio.h>

int main(){
    
    int n;
    int input, prior;
    int q;
    int x, y;
    int sum[100000];

    scanf("%d", &n);
    scanf("%d", &prior); 

    for(int i = 1; i < n; i++){
        scanf("%d", &input);

        sum[i-1] += prior > input ? 1 : 0;
        sum[i] = sum[i-1];
        prior = input;
    }

    scanf("%d", &q);
    for(int i = 0; i < q; i++){
        scanf("%d %d", &x, &y);

        if (y == 1) {
            printf("%d\n", 0);
        } else if (x == 1) {
            printf("%d\n", sum[y-2]);
        } else {
            printf("%d\n", sum[y-2] - sum[x-2]);
        }        
    }

    return 0;
}

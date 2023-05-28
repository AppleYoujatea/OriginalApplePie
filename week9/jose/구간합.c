# c 쫌 짱인듯.
#include <stdio.h> 

int main(){
    int n, m;
    int arr[1024 * 1024 + 1];
    int temp; 
    int x1, y1, x2, y2;
    int sum;

    scanf("%d %d", &n, &m);
    
    for(int i = 0; i < n * n; i++){
        scanf("%d", &temp);
        arr[i + 1] = arr[i] + temp;
    }

    for(int i = 0; i < m; i++){
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
        sum = 0;
        for(int j = 0; j < x2-x1 + 1; j++){
            temp = arr[((x1 - 1) + j) * n + y2] - arr[((x1 - 1) + j) * n + y1 - 1];
            sum += temp;
        }
        printf("%d\n", sum);
    }

    return 0;
}

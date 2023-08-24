#include<string.h>
#include <stdio.h>
const int N = 26;

int main() {
    // Write C code here
    char* compString;
    scanf("%s", compString);
    int count[N];
    
    for(int i=0; i<strlen(compString); i++){
        count[compString[i]-'a'+1]++;
    }
    int total=0;
    for(int i=0; i<N; i++){
        if(count[i]==1){
            total++;
        }
    }
    printf("%d", total+1);

    return 0;
}
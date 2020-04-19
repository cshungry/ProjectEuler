#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define LL unsigned long long
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    LL tc,n;
    cin>>tc;
    while(tc--){
        cin>>n;
        LL suma,sumb,sum;
        suma=(n*(n+1))/2;
        sumb=(n*(n+1)*(2*n+1))/6;
        //cout<<"suma "<<suma<<endl;
        //cout<<"sumb "<<sumb<<endl;
        sum=pow(suma,2)-sumb;
        cout<<sum<<endl;
    }
    return 0;
}

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define LL unsigned long long
LL fibo(LL n){
    vector<LL> v={1,2};
    LL sum=2,i=2;
    while(true){
        if(v[i-1]>n)break;
        v.push_back(v[i-1]+v[i-2]);
        if(v[i]%2==0 && v[i]<n)sum+=v[i];
        i++;
    }
    
    return sum;
}
int main() {
    LL tc,n;
    cin>>tc;
    while(tc--){
        cin>>n;
        LL sum=fibo(n);
        cout<<sum<<endl;
    }
    return 0;
}

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define LL unsigned long long
LL gcd(LL a,LL b){
    if(a%b==0)return b;
    return gcd(b,a%b);
}
LL lcm(LL n){
    LL l=1;
    for(LL i=2;i<=n;i++){
        l=(l*i)/gcd(l,i);
    }
    return l;
}

int main() {
    LL tc,n;
    cin>>tc;
    while(tc-- ){
        cin>>n;
        LL l=lcm(n);
        cout<<l<<endl;
    }
    return 0;
}

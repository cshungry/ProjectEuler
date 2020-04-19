#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define LL long long
bool prime(LL n){
    for(LL i=2;i*i<=n;i++){
        if(n%i==0)return false;
    }
    return true;
}
LL factor(LL n){
    LL l=1;
    while(n%2==0){
        l=2;
        n/=2;

    }
    for(LL i=3;i*i<=n;i+=2){
        bool flag=false;
        while(n%i==0){
            n/=i;
            flag=true;
        }
        if(flag==true){
            if(prime(i)==true && i>l)l=i;
        }
    }
    if(n>2){
        if(prime(n) && n>l)l=n;
    }
    return l;
}
int main() {
    LL tc,n;
    cin>>tc;
    while(tc--){
        cin>>n;
        LL l=factor(n);
        cout<<l<<endl;
    }
    return 0;
}

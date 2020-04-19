#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#define LL unsigned long long 
int vis[10002];
LL lvis=1;
bool isprime(LL n){
    for(LL ind=2;ind*ind<=n;ind++){
        if(n%ind==0)return false;
    }
    return true;
}
LL prime(LL n){
    //cout<<lvis<<" lvis\n";
    LL i=vis[lvis]+1;
    while(true){
        if(isprime(i)){
            lvis++;
            vis[lvis]=i;
            if(lvis==n)break;
        }
        i++;
    }
    return vis[lvis];
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    vis[1]=2;   
    LL tc,n;
    cin>>tc;
    while(tc--){
        cin>>n;
        if(vis[n]!=0){
            cout<<vis[n]<<endl;
        }
        else{
            cout<<prime(n)<<endl;
        }
    }
    //for(int i=1;i<10;i++)cout<<vis[i]<<" ";
    return 0;
}

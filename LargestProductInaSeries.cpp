#include<bits/stdc++.h>
using namespace std;

#define LL unsigned long long
LL mul(string sub){
    LL num,prod=1;
    num=stoi(sub);
    //cout<<num<<endl;
    while(num>0){
        int rem=num%10;
        prod*=rem;
        num/=10;
    }
    return prod;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int tc,n,k;
    string s;
    cin>>tc;
    while(tc--){
        cin>>n>>k>>s;
        LL prod;
        string sub;
        sub=s.substr(0,k);
    
        prod=mul(sub);
        //cout<<"sub "<<sub<<" prod "<<prod<<endl;
        for(int i=1;i<s.length()-k;i++){
            sub=s.substr(i,k);
            LL check=mul(sub);
            //cout<<"sub "<<sub<<" prod "<<check<<endl;
            if(check>prod)prod=check;
        }
        cout<<prod<<endl;
    } 
    return 0;
}

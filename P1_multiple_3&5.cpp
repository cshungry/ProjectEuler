#include <bits/stdc++.h>
using namespace std;
#define LL long long

int main() {
   LL tc,n;
   cin>>tc;
   while(tc--){
       cin>>n;
       n--;
       LL a=n/3,b=n/5,c=n/15;
       LL suma,sumb,sumc,sum;
       suma=(a*(6+(a-1)*3))/2;
       sumb=(b*(10+(b-1)*5))/2;
       sumc=(c*(30+(c-1)*15))/2;
       sum=suma+sumb-sumc;
       cout<<sum<<endl;
   }
   return 0;
}

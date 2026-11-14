int mod_inv(long long int n,long long int mod){
    long long int m=mod-2;
    long long int temp=n;
    long long int ans=1;
    while (true){
        if (m%2==1){
            ans=(ans*temp)%mod;
        }
        temp=(temp*temp)%mod;
        m=m/2ll;
        if (m==0ll){
            return ans;
        }
    }
}
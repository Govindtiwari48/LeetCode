class Solution {
public:
    vector<int> findArray(vector<int>& pref) {
        int p=0,i=0,n=pref.size();
        vector<int> res;
        while(i<n)
        {
            res.push_back(pref[i]^p);
            p=pref[i];
            i++;
        }
        return res;
        
    }
};
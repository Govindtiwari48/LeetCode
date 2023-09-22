/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    private:
    void inorder(vector<int>&v,TreeNode* root)
    {
        if(root==NULL)
        return;
        inorder(v,root->left);
        v.push_back(root->val);
        inorder(v,root->right);
    } 
    vector<int>inorderTraversal(TreeNode* root)
    {
        vector<int>v;
        inorder(v,root);
        return v;
    }
public:
    TreeNode* increasingBST(TreeNode* root) {
    vector<int>ans;
    TreeNode* dummy=new TreeNode();
    TreeNode* curr=dummy;
    ans=inorderTraversal(root);
    for(int i=0;i<ans.size();i++)
    {
        curr->right=new TreeNode(ans[i]);
        curr=curr->right;
    }
    return dummy->right;
    }
};
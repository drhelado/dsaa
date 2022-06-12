class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res=[]
        s=''
        for x in searchWord:
            s=s+x
            c=0
            ans=[]
            for p in products:
                if p.startswith(s):
                    c=c+1
                    if c<4:
                        ans.append(p)
            res.append(ans)
        return (res) 

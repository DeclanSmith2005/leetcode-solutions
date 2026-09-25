class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        parents = [i for i in range(len(accounts))]

        def union(a, b):
            a = find(a)
            b = find(b)
            parents[a] = parents[b]
        
        def find(a):
            while a != parents[a]:
                a = parents[a]
            return a
    
        emailToAccount = {} # emails -> account

        for i, acc in enumerate(accounts):
            for k in range(1, len(acc)):
                email = acc[k]
                if email in emailToAccount:
                    union(emailToAccount[email], i)
                emailToAccount[email] = find(i)

        children = defaultdict(lambda: set()) # parentIndex -> set(associated emails)
        # accumulate all associated emails with their parents in children dict
        for i, acc in enumerate(accounts):
            parent = find(i)
            for k in range(1, len(acc)):
                email = acc[k]
                children[parent].add(email)
        
        return [
            [accounts[parent][0]] + sorted(emails)
            for parent, emails in children.items()
        ]

            
                
            


                    

                    

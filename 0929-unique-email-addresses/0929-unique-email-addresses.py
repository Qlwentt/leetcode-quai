class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        setEmails = set()
        
        for email in emails:
            localName, domainName = email.split('@')
            localName = localName.replace(".", "")
            plusI = localName.find("+")
            if plusI != -1:
                localName = localName[:plusI]
            setEmails.add(localName+"@"+domainName)        
        return len(setEmails)
            
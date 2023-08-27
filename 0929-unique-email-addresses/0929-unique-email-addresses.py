class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        filteredEmails = set()
        for email in emails:
            localName, domainName = email.split("@")
            localName = localName.replace(".", "")
            plusIndex = localName.find('+')
            if plusIndex != -1:
                localName = localName[:plusIndex]
            filteredEmail = localName + "@" + domainName
            filteredEmails.add(filteredEmail)
        return len(filteredEmails)
            
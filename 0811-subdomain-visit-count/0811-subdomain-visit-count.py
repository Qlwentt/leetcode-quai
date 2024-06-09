class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = collections.defaultdict(int)
        
        for info in cpdomains:
            num, full_domain = info.split(" ")
            num = int(num)
            dot = full_domain.find(".")
            second_dot = full_domain.find(".", dot+1)
            second_dot = None if second_dot == -1 else second_dot
            counts[full_domain] += num
            counts[full_domain[dot+1:]] += num
            if second_dot:
                counts[full_domain[second_dot+1:]] += num
        answer = []
        for domain, hits in counts.items():
            answer.append(f'{hits} {domain}')
        
        return answer
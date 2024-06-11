class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def custom_sort(x):
            i, log = x
            log = log.split(" ")
            log_type = "digit" if log[1].isnumeric() else "let"
            identifier = log[0]
            contents = log[1:]
            return (log_type != "let", (contents,identifier) if log_type == "let" else i)
        logs = list(enumerate(logs))
        logs.sort(key=lambda a: custom_sort(a))
        logs = [element for index, element in logs]

        return logs
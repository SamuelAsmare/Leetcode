class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for item in paths:
            each_part = item.split(" ")
            directory = each_part[0]
            for files in each_part[1:]:
                arr = files.split("(")
                file_name = arr[0]
                component = arr[1][:-1]
                full_dir = f"{directory}/{file_name}"
                group[component].append(full_dir)
        ans = []
        return [collection for collection in group.values() if len(collection)>1]


                




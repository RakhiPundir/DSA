class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        
        for index in range(len(candidates)):
		
            for sub_target in range(1, target + 1):
			
                if candidates[index] == sub_target:
                    dp[sub_target].append([candidates[index]])
					
                elif candidates[index] < sub_target:
                    remaining_sub_target = sub_target - candidates[index]

                    for remaining_possibility in dp[remaining_sub_target]:
                        dp[sub_target].append([candidates[index]] + remaining_possibility)
        
        return dp[target]

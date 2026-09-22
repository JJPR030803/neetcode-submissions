func twoSum(nums []int, target int) []int {
    seen := make(map[int]int)
	indices := []int{}
	for i,num := range nums{
		t := target - num
		if idx, ok := seen[t]; ok{
			indices = append(indices,idx)
			indices = append(indices,i)
			return indices
		}
		seen[num] = i
	}
	return indices
}

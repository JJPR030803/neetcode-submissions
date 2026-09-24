func removeElement(nums []int, val int) int {
	
    pointer := 0

	for i := 0; i < len(nums); i++{
		if nums[i] != val{
			nums[pointer] = nums[i]
			pointer++
		}else if nums[i] == val{
			continue
		}
	}
	return pointer
}

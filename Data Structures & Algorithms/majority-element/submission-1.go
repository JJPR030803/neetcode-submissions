func majorityElement(nums []int) int {
    counter := make(map[int]int)
	max := math.MinInt
	result := 0
	for _,num := range nums{
		if _,ok := counter[num]; ok{
			counter[num]++
		}else{
			counter[num] = 1
		}
	}
	for k,v := range counter{
		if v > max{
			max = v
			result = k
		}
	}
	return result
}

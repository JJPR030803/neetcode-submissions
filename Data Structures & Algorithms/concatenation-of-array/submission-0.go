func getConcatenation(nums []int) []int {
	acc := make([]int,0,len(nums)*2)
    acc = append(acc,nums...)
	acc = append(acc,nums...)
	return acc
}

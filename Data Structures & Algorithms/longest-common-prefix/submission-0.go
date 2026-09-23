func longestCommonPrefix(strs []string) string {
    
	for i := 0; i <len(strs[0]); i++{

		char := strs[0][i]

		for _, str := range strs[1:]{
			if i == len(str) || str[i] != char{
				return strs[0][:i]
			}
		}
	}
	return strs[0]
	}

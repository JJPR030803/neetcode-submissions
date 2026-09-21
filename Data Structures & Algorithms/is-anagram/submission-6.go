func isAnagram(s string, t string) bool {
    if len(s) != len(t){
        return false
    }
    counts := make(map[rune]int)
    for _,ch := range s{
        counts[ch]++
    }

    for _, ch := range t{
        if _,ok := counts[ch]; !ok{
            return false
        }

        if n,ok := counts[ch]; ok && n >= 1{
            counts[ch]--
        }else{
            return false
        }
    }


    return true

}

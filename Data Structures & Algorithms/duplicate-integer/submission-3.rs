impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let mut set = HashSet::new();
        nums.iter().any(|n| !set.insert(n))
    }
}

import java.util.HashSet;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> numSet = new HashSet<Integer>();
        for (int num : nums) 
        { 
            numSet.add(num);
        }
        return nums.length != numSet.size();
    }
}
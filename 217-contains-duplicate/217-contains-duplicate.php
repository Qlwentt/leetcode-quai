class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function containsDuplicate($nums) {
        $hashSet = [];
        foreach ($nums as $num) {
            if (!array_key_exists($value, $hashSet)) {
                $hashSet[$num] = true;
            }
        }
        return count($hashSet) != count($nums);
    }
}
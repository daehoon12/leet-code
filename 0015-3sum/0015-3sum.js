/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    let answer = new Set();
    nums.sort((a, b) => a - b);
    for (let i = 0; i < nums.length; i++) {
        let low = i + 1;
        let high = nums.length - 1;
        while (low < high) {
            let sum = nums[i] + nums[low] + nums[high];
            if (sum === 0) {
                answer.add(JSON.stringify([nums[i], nums[low], nums[high]]));
                low++;
                high--;
            } else if (sum > 0) {
                high--;
            } else {
                low++;
            }
        }
    }
    return Array.from(answer).map(JSON.parse);
};

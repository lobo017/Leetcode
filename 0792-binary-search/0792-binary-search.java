class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length-1;
        int mid = (r+l)/2;

        // if(nums[mid] > target){
        //     for(int i = nums[mid]; i >= l; i--){
        //         if(nums[i] == target){
        //             return i;
        //         }
        //     }
        // }else if(nums[mid] < target){
        //     for(int j = nums[mid]; j <= r; j++){
        //         if(nums[j] == target){
        //             return j;
        //         }
        //     }
        // }else if(nums[mid] == target){
        //     return mid;
        // }else{
        //     return -1;
        // }
        // return -1;

        while(l<=r){
            mid = (r+l)/2;
            if(nums[mid] > target){
                r = mid -1;
            }else if(nums[mid] < target){
                l = mid +1;
            }else{
                return mid;
            }
        }
        return -1;
    }
}
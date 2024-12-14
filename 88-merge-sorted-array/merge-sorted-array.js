var merge = function(nums1, m, nums2, n) {
    let a = m - 1
    let b = n - 1
    let k = m + n - 1

    while (a >= 0 && b >= 0) {
        if (nums1[a] > nums2[b]) {
            nums1[k] = nums1[a]
            a -=1
        }
        else {
            nums1[k] = nums2[b]
            b -=1
        }
        k -= 1
    }

    while (a >= 0) {
        nums1[k--] = nums1[a--]
    }

    while (b >= 0) {
        nums1[k --] = nums2[b--]
    }

};
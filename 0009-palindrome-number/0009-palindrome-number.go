func isPalindrome(x int) bool {
		if x < 0{
	return false
	}
	str:= strconv.Itoa(x)
	n :=len(str)
	for i:=0 ;i< n/2;i++{
		if str[i] != str[n-i-1]{
			return false
		}
	}
	return true

}

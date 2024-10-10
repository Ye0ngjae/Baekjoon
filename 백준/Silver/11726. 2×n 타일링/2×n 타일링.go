package main

import (
	"fmt"
	"runtime"
)

func main() {
	runtime.GOMAXPROCS(runtime.NumCPU())

	var N int
	fmt.Scan(&N)
	DP := [1001]int{}

	DP[1] = 1
	DP[2] = 2

	for i := 3; i <= N; i++ {
		DP[i] = (DP[i-1] + DP[i-2]) % 10007
	}

	fmt.Println(DP[N])
}

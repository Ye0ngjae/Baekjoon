package main

import (
	"fmt"
	"runtime"
)

func main() {
	runtime.GOMAXPROCS(runtime.NumCPU())

	var N int
	fmt.Scan(&N)
	DP := [1000000][2]int{}

	DP[1][0] = 0
	DP[1][1] = 1

	for i := 2; i < N+1; i++ {
		DP[i][0] = DP[i-1][0] + DP[i-1][1]
		DP[i][1] = DP[i-1][0]
	}

	fmt.Println(DP[N][0] + DP[N][1])
}

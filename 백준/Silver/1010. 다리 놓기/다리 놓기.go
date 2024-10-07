package main

import (
	"fmt"
	"runtime"
)

func main() {
	runtime.GOMAXPROCS(runtime.NumCPU())

	T := 0
	var DP [31][31]int

	for i := 0; i < 31; i++ {
		DP[i][1] = i
		DP[i][0] = 1
		DP[i][i] = 1
	}

	for i := 2; i < 31; i++ {
		for j := 1; j < i; j++ {
			DP[i][j] = DP[i-1][j] + DP[i-1][j-1]
		}
	}

	fmt.Scan(&T)

	for i := 0; i < T; i++ {
		N := 0
		M := 0

		fmt.Scan(&N, &M)
		fmt.Println(DP[M][N])

	}
}

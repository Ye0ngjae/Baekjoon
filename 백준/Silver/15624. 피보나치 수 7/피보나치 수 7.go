package main

import (
	"fmt"
	"runtime"
)

func main() {
	runtime.GOMAXPROCS(runtime.NumCPU())

	var N int
	fmt.Scan(&N)
	fibo := make([]int, 1)

	for i := 1; i <= N; i++ {
		if i == 1 || i == 2 {
			fibo = append(fibo, 1)
			continue
		}
		fibo = append(fibo, fibo[i-1]+fibo[i-2])
	}

	fmt.Println(fibo[N]%1000000007)

}

package main

import (
	"fmt"
	"runtime"
)

func main() {
	runtime.GOMAXPROCS(runtime.NumCPU())

	N := 0
	var A, B, X int64

	fmt.Scan(&N)

	for i := 0; i < N; i++ {
		fmt.Scan(&A, &B, &X)

		fmt.Println(A*(X-1) + B)
	}
}

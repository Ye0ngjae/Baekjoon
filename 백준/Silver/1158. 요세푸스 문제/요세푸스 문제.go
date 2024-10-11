package main

import (
	"fmt"
	"runtime"
	"strconv"
	"strings"
)

func main() {
	runtime.GOMAXPROCS(runtime.NumCPU())

	var N int
	var K int

	result := []int{}

	fmt.Scan(&N, &K)
	man := []int{}

	for i := 0; i < N; i++ {
		man = append(man, i+1)
	}

	cur := 0
	now := 0

	for {
		if len(result) == N {
			break
		}

		if man[now] != 0 {
			cur++

			if cur == K {
				result = append(result, man[now])
				man[now] = 0
				cur = 0
			}
		}
		if now == N-1 {
			now = 0
		} else {
			now++
		}
	}

	output := []string{}

	for i := 0; i < len(result); i++ {
		output = append(output, strconv.Itoa(result[i]))
	}

	ans := "<"
	ans += strings.Join(output, ", ")
	ans += ">"

	fmt.Println(ans)

}

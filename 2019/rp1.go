package main

import (
	"fmt"
	"strings"
)

func main() {
	var t int
	fmt.Scanf("%d", &t)
	for i := 1; i <= t; i++ {
		var a, b, n int
		fmt.Scanf("%d %d", &a, &b)
		a = a + 1
		fmt.Scanf("%d", &n)
		for {
			m := (a + b) / 2
			fmt.Println(m)
			var str string
			fmt.Scanf("%s", &str)
			if strings.EqualFold(str, "CORRECT") {
				break
			} else if strings.EqualFold(str, "TOO_SMALL") {
				a = m + 1
			} else if strings.EqualFold(str, "TOO_BIG") {
				b = m - 1
			}
		}
	}
}

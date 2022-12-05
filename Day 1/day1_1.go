package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func main() {

	file, err := os.Open("data")
	if err != nil {
		fmt.Printf("Could not read the file due to this %s error \n", err)
	}

	var listOfTotals []int
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	file.Close()
	count := 0

	for index, _ := range lines {

		if lines[index] == "" {

			high := index
			low := high - count + 1
			listOfTotals = append(listOfTotals, sumRange(lines[low:high]))

			count = 0
		}

		if index == len(lines)-1 {
			high := index
			low := high - count + 1
			listOfTotals = append(listOfTotals, sumRange(lines[low:index+1]))
			count = 0
		}
		count = count + 1
	}
	sort.Ints(listOfTotals)
	last := len(listOfTotals) - 1
	fmt.Println(listOfTotals[last])
}

func sumRange(lines []string) int {
	total := 0
	for totIndex, _ := range lines {
		conNum := 0
		conNum, err := strconv.Atoi(lines[totIndex])
		if err != nil {
			panic(err)
		}
		total = total + conNum

	}
	return total
}
package main

import (
	"container/list"
	"fmt"
)

// 덱 자료 구조
type Deque struct {
	v *list.List
}

func NewDeque() *Deque {
	return &Deque{list.New()}
}

func (d *Deque) Extend(v interface{}) {
	d.v.PushBack(v)
}

func (d *Deque) Extendleft(v interface{}) {
	d.v.PushFront(v)
}

func (d *Deque) Pop() interface{} {
	back := d.v.Back()
	if back == nil {
		return nil
	}

	return d.v.Remove(back)
}

func (d *Deque) Popleft() interface{} {
	front := d.v.Front()
	if front == nil {
		return nil
	}

	return d.v.Remove(front)
}

func main() {

	var N int

	card := NewDeque()

	fmt.Scan(&N)

	for i := 1; i <= N; i++ {
		card.Extend(i)
	}

	for {
		if card.v.Len() == 1 {
			break
		}

		fmt.Print(card.Popleft(), " ")
		card.Extend(card.Popleft())

	}

	fmt.Println(card.Popleft())
}

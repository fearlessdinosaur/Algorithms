package main

import "fmt"

// data structure for indivdual nodes
type Node struct {

  data int
  next *Node

}

func main() {
  // start Declarations
  head := Node{12,nil}
  fmt.Printf("%d", head.data)
  // end Declarations

  // Test function calls
  append( 13,&head )
  append( 15,&head )
  traverse( &head )
  pop( &head )
  traverse( &head )

}

//function to add new node to the stack
func append( x int, tail *Node ){

  if( tail.next != nil ){
    append( x,tail.next )
  }else {
    tail.next = &Node{x,nil}
    tail = tail.next
  }

}

// function to remove base node from the stack
func pop( tail *Node ){

  if( tail.next.next != nil ){
    pop( tail.next )
  }else{
    tail.next = nil
  }

}

// function to traverse and print the stack
func traverse(top *Node){

  fmt.Printf( "%d\n",top.data )

  if(top.next != nil){
    traverse( top.next )
  }else{
    fmt.Printf( "End of the line" )
  }

}

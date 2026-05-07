object IfElseExample {
  def main(args: Array[String]): Unit = {
    println("Enter a number: ")

    val number = scala.io.StdIn.readInt()  // Read user input

    if (number > 0) {
      println(s"$number is Positive")
    } else if (number < 0) {
      println(s"$number is Negative")
    } else {
      println("The number is Zero")
    }
  }
}

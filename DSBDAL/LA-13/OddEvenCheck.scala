object OddEvenCheck {
  def main(args: Array[String]): Unit = {
    println("Enter a number: ")

    // Read user input as string and convert to Int
    val number = scala.io.StdIn.readInt()

    // Check if number is even or odd
    if (number % 2 == 0) {
      println(s"$number is Even")
    } else {
      println(s"$number is Odd")
    }
  }
}

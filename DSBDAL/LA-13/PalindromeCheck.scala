object PalindromeChecker {
  def main(args: Array[String]): Unit = {
    println("Enter a string: ")
    
    val input = scala.io.StdIn.readLine()           // Read string from user
    val cleanInput = input.toLowerCase.replaceAll("\\W", "") // ignore case & non-letters

    if (cleanInput == cleanInput.reverse) {
      println(s"'$input' is a palindrome")
    } else {
      println(s"'$input' is NOT a palindrome")
    }
  }
}

object WordCo {
  def main(args: Array[String]): Unit = {
    val text = "Hello world hello Scala world"

    val words = text.toLowerCase.split("\\W+")

    // Fix: use map instead of mapValues
    val wordCount = words
      .groupBy(identity)                 // Map[String, Array[String]]
      .map { case (word, arr) => (word, arr.length) } // convert to (word, count)

    wordCount.foreach { case (word, count) =>
      println(s"$word: $count")
    }
  }
}

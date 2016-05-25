//Check whether a function is palindrome or not

func is_palindrome(s: String) -> (Bool) {
  let reversed_str = String(s.characters.reverse())
  if(s == reversed_str) {
    return true
  } else {
    return false
  }
}

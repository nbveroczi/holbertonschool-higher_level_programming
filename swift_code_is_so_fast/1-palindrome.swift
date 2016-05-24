/* This is a function to see if a string is a palindrome */
func is_palindrome(s: String) -> (Bool)
{
    
    let reversed_string = String(s)
    
    if (reversed_string == s) {
        return true
    } else {
        return false
    }
}


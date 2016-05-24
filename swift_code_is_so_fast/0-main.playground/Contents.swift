//: Playground - noun: a place where people can play

//import UIKit

//var str = "Hello, playground"
import Cocoa

//Assigning a value to a String variable
var str = "Hello, playground"

//Create empty character Array.
var strArray:Character[] = Character[]()

//Loop through each character in the String
for character in str {
    //Insert the character in the Array variable.
    strArray.append(character)
}

//Create a empty string
var reversedStr:String = ""

//Read the array from backwards to get the characters
for var index = strArray.count - 1; index >= 0;--index {
    //Concatenate character to String.
    reversedStr += strArray[index]
}

reversedStr



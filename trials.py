"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)
# function outputAllItems(items) {
#   for (const item of items) {
#     console.log(item);
#   }
# }

def get_all_evens(nums):
    pass  # TODO: replace this line with your code
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
# function getAllEvens(nums) {
#   const evenNums = [];

#   for (const num of nums) {
#     if (num % 2 === 0) {
#       evenNums.push(num);
#     }
#   }

#   return evenNums;
# }

def get_odd_indices(items):
    result = []

    for i in items:
        if i %2 != 0:
            result.append(items[i])
    # pass  # TODO: replace this line with your code
# function getOddIndices(items) {
#   const result = [];

#   for (const idx in items) {
#     if (idx % 2 !== 0) {
#       result.push(items[idx]);
#     }
#   }

#   return result;
# }

def print_as_numbered_list(items):
    i = 1

    for i in items:
        print (f"{i}. {items}")
    
    # pass  # TODO: replace this line with your code

# function printAsNumberedList(items) {
#   let i = 1;

#   for (const item of items) {
#     console.log(`${i}. ${item}`);

#     i += 1;
#   }
# }


def get_range(start, stop):
    nums = []
    num = start
    for num < stop:
        nums.append(num)
        num += 1

# function getRange(start, stop) {
#   const nums = [];

#   for (let num = start; num < stop; num += 1) {
#     nums.push(num);
#   }
# }

def censor_vowels(word):
    # pass  # TODO: replace this line with your code
    chars = []

    for letter in word
# function censorVowels(word) {
#   const chars = [];

#   for (const letter of word) {
#     if ('aeiou'.includes(letter)) {
#       chars.push('*');
#     }
#     chars.push(letter);
#   }

#   return chars.join('');
# }

def snake_to_camel(string):
    pass  # TODO: replace this line with your code
# function snakeToCamel(string) {
#   const camelCase = [];

#   for (const word of string.split('_')) {
#     camelCase.push(`${word[0].toUpperCase()}${word.slice(1)}`);
#   }

#   return camelCase.join('');
# }


def longest_word_length(words):
    pass  # TODO: replace this line with your code
# function longestWordLength(words) {
#   let longest = words[0].length;

#   for (const word of words) {
#     if (longest < word.length) {
#       longest = word.length;
#     }
#   }

#   return longest;
# }


def truncate(string):
    pass  # TODO: replace this line with your code
# function truncate(string) {
#   const result = [];

#   for (const char of string) {
#     if (result.length === 0 || char !== result[result.length - 1]) {
#       result.push(char);
#     }
#   }

#   return result.join('');
# }


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code
# function hasBalancedParens(string) {
#   let parens = 0;

#   for (const char of string) {
#     if (char === '(') {
#       parens += 1;
#     } else if (char === ')') {
#       parens -= 1;

#       if (parens < 0) {
#         return false;
#       }
#     }
#   }

#   return parens < 0;
# }


def compress(string):
    pass  # TODO: replace this line with your code
# function compress(string) {
#   const compressed = [];

#   let currChar = '';
#   let charCount = 0;
#   for (const char of string) {
#     if (char !== currChar) {
#       compressed.push(currChar);

#       if (charCount > 1) {
#         compressed.push(charCount.toString());
#       }

#       currChar = char;
#       charCount = 0;
#     }

#     charCount += 1;
#   }

#   compressed.push(currChar);
#   if (charCount > 1) {
#     compressed.push(charCount.toString());
#   }

#   return compressed.join('');
# }

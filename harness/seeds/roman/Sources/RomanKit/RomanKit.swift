/// RomanKit converts between integers and Roman numerals.
///
/// Contract (the implementation must satisfy this):
/// - Valid range is 1...3999.
/// - Standard *subtractive* notation is required:
///     4 == "IV", 9 == "IX", 40 == "XL", 90 == "XC", 400 == "CD", 900 == "CM".
///   e.g. 1994 == "MCMXCIV", 3999 == "MMMCMXCIX".
/// - `toRoman` throws `RomanError.outOfRange` when n < 1 or n > 3999.
/// - `fromRoman` parses a valid Roman numeral string and returns its Int value,
///   correctly handling subtractive pairs (so "IV" == 4, not 6).
/// - `fromRoman(toRoman(n)) == n` for every n in 1...3999.

public enum RomanError: Error, Equatable {
    case outOfRange
    case invalidCharacter(Character)
}

private let symbols: [(value: Int, symbol: String)] = [
    (1000, "M"), (500, "D"), (100, "C"), (50, "L"), (10, "X"), (5, "V"), (1, "I"),
]

public func toRoman(_ n: Int) throws -> String {
    guard n >= 1 && n <= 3999 else { throw RomanError.outOfRange }
    var remaining = n
    var result = ""
    for entry in symbols {
        while remaining >= entry.value {
            result += entry.symbol
            remaining -= entry.value
        }
    }
    return result
}

private let charValue: [Character: Int] = [
    "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
]

public func fromRoman(_ s: String) throws -> Int {
    var total = 0
    for ch in s {
        guard let v = charValue[ch] else { throw RomanError.invalidCharacter(ch) }
        total += v
    }
    return total
}

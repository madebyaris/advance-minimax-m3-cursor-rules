import XCTest
@testable import RomanKit

// HIDDEN grader -- copied into Tests/RomanKitTests/ only AFTER the agent finishes.
final class HiddenRomanTests: XCTestCase {
    func testToRomanHidden() throws {
        XCTAssertEqual(try toRoman(40), "XL")
        XCTAssertEqual(try toRoman(90), "XC")
        XCTAssertEqual(try toRoman(400), "CD")
        XCTAssertEqual(try toRoman(900), "CM")
        XCTAssertEqual(try toRoman(58), "LVIII")
        XCTAssertEqual(try toRoman(1994), "MCMXCIV")
        XCTAssertEqual(try toRoman(2024), "MMXXIV")
        XCTAssertEqual(try toRoman(3999), "MMMCMXCIX")
    }

    func testFromRomanHidden() throws {
        XCTAssertEqual(try fromRoman("XL"), 40)
        XCTAssertEqual(try fromRoman("CM"), 900)
        XCTAssertEqual(try fromRoman("MCMXCIV"), 1994)
        XCTAssertEqual(try fromRoman("MMMCMXCIX"), 3999)
        XCTAssertEqual(try fromRoman("LVIII"), 58)
    }

    func testRoundTrip() throws {
        for n in [1, 4, 9, 14, 40, 44, 99, 444, 999, 1666, 2024, 3999] {
            XCTAssertEqual(try fromRoman(try toRoman(n)), n)
        }
    }

    func testOutOfRange() {
        XCTAssertThrowsError(try toRoman(0))
        XCTAssertThrowsError(try toRoman(4000))
    }
}
